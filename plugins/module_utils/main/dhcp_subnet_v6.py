from ansible.module_utils.basic import AnsibleModule

from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.api import \
    Session
from ansible_collections.fyrastack.opnsense.plugins.module_utils.helper.main import \
    get_selected_list, simplify_translate
from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.cls import BaseModule


class SubnetV6(BaseModule):
    CMDS = {
        'add': 'add_subnet',
        'del': 'del_subnet',
        'set': 'set_subnet',
        'search': 'search_subnet',
        'detail': 'get_subnet',
    }
    API_KEY = 'subnet6'
    API_KEY_PATH = 'subnet6'
    API_MOD = 'kea'
    API_CONT = 'dhcpv6'
    API_CONT_REL = 'service'
    FIELDS_CHANGE = [
        'subnet', 'description', 'interface', 'pools', 'auto_options',
        'dns', 'domain_search', 'v6_dnr', 'valid_lifetime',
    ]
    FIELDS_ALL = FIELDS_CHANGE
    FIELDS_TYPING = {
        'list': ['dns', 'domain_search'],
        'bool': ['auto_options'],
        'int': ['valid_lifetime'],
        'select': ['interface'],
    }
    FIELDS_TRANSLATE = {
        'auto_options': 'option_data_autocollect',
    }
    API_ATTR_OPTIONS = 'option_data'
    API_FIELDS_OPTIONS = [
        'dns', 'domain_search', 'v6_dnr',
    ]
    POOL_JOIN_CHAR = '\n'
    FIELDS_TRANSLATE_SPECIAL = {
        'dns': 'dns_servers',
        'v6_dnr': 'v6_dnr',
    }
    EXIST_ATTR = 'subnet'

    def __init__(self, module: AnsibleModule, result: dict, session: Session = None, fail: dict = None):
        BaseModule.__init__(self=self, m=module, r=result, s=session, f=fail)
        self.subnet = {}
        self.existing_subnets = None

    def _split_pools(self, pools) -> list:
        if isinstance(pools, list):
            return pools

        if pools in [None, '']:
            return []

        return pools.split(self.POOL_JOIN_CHAR)

    def _simplify_existing(self, entry: dict) -> dict:
        simple = simplify_translate(
            existing=entry,
            typing=self.FIELDS_TYPING,
            translate=self.FIELDS_TRANSLATE,
            ignore=self.API_FIELDS_OPTIONS,
        )

        simple['pools'] = self._split_pools(simple['pools'])
        if self.API_ATTR_OPTIONS in entry:
            opts = entry[self.API_ATTR_OPTIONS]
            return {
                **simple,
                'dns': get_selected_list(opts[self.FIELDS_TRANSLATE_SPECIAL['dns']], remove_empty=True),
                'domain_search': get_selected_list(opts['domain_search'], remove_empty=True),
                'v6_dnr': opts[self.FIELDS_TRANSLATE_SPECIAL['v6_dnr']],
            }

        return {
            **simple,
            'dns': get_selected_list(entry[f"option_data.{self.FIELDS_TRANSLATE_SPECIAL['dns']}"], remove_empty=True),
            'domain_search': get_selected_list(entry['option_data.domain_search'], remove_empty=True),
            'v6_dnr': entry[f"option_data.{self.FIELDS_TRANSLATE_SPECIAL['v6_dnr']}"],
        }

    def _build_request(self) -> dict:
        raw_request = self.b.build_request(ignore_fields=self.API_FIELDS_OPTIONS)

        raw_request[self.API_KEY]['pools'] = self.POOL_JOIN_CHAR.join(self.p['pools'])
        raw_request[self.API_KEY][self.API_ATTR_OPTIONS] = {
            self.FIELDS_TRANSLATE_SPECIAL['dns']: self.b.RESP_JOIN_CHAR.join(self.p['dns']),
            'domain_search': self.b.RESP_JOIN_CHAR.join(self.p['domain_search']),
            self.FIELDS_TRANSLATE_SPECIAL['v6_dnr']: self.p['v6_dnr'],
        }

        return raw_request
