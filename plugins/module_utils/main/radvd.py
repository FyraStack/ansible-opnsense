from ansible.module_utils.basic import AnsibleModule

from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.api import \
    Session
from ansible_collections.fyrastack.opnsense.plugins.module_utils.helper.main import \
    get_selected_list, simplify_translate
from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.cls import BaseModule


class Radvd(BaseModule):
    CMDS = {
        'add': 'add_entry',
        'del': 'del_entry',
        'set': 'set_entry',
        'search': 'search_entry',
        'detail': 'get_entry',
        'toggle': 'toggle_entry',
    }
    API_KEY = 'entries'
    API_KEY_PATH = 'entries'
    API_MOD = 'radvd'
    API_CONT = 'settings'
    API_CONT_REL = 'service'
    FIELDS_CHANGE = [
        'enabled', 'interface', 'base6_interface', 'mode',
        'deprecate_prefix', 'remove_adv_on_exit', 'remove_route',
        'routes', 'rdnss', 'dnssl', 'dns',
        'min_interval', 'max_interval', 'dnssl_lifetime',
        'default_lifetime', 'link_mtu', 'preferred_lifetime',
        'ra_src_address', 'rdnss_lifetime', 'route_lifetime',
        'valid_lifetime', 'default_preference', 'nat64prefix',
        'hop_limit',
    ]
    FIELDS_ALL = FIELDS_CHANGE
    FIELDS_TRANSLATE = {
        'base6_interface': 'Base6Interface',
        'deprecate_prefix': 'DeprecatePrefix',
        'remove_adv_on_exit': 'RemoveAdvOnExit',
        'remove_route': 'RemoveRoute',
        'rdnss': 'RDNSS',
        'dnssl': 'DNSSL',
        'min_interval': 'MinRtrAdvInterval',
        'max_interval': 'MaxRtrAdvInterval',
        'dnssl_lifetime': 'AdvDNSSLLifetime',
        'default_lifetime': 'AdvDefaultLifetime',
        'link_mtu': 'AdvLinkMTU',
        'preferred_lifetime': 'AdvPreferredLifetime',
        'ra_src_address': 'AdvRASrcAddress',
        'rdnss_lifetime': 'AdvRDNSSLifetime',
        'route_lifetime': 'AdvRouteLifetime',
        'valid_lifetime': 'AdvValidLifetime',
        'default_preference': 'AdvDefaultPreference',
        'hop_limit': 'AdvCurHopLimit',
    }
    FIELDS_TYPING = {
        'bool': ['enabled', 'dns'],
        'int': [
            'min_interval', 'max_interval', 'dnssl_lifetime',
            'default_lifetime', 'link_mtu', 'preferred_lifetime',
            'rdnss_lifetime', 'route_lifetime', 'valid_lifetime',
            'hop_limit',
        ],
        'list': ['routes', 'rdnss', 'dnssl'],
        'select': [
            'interface', 'base6_interface', 'mode', 'deprecate_prefix',
            'remove_adv_on_exit', 'remove_route', 'default_preference',
        ],
    }
    INT_VALIDATIONS = {
        'min_interval': {'min': 3},
        'max_interval': {'min': 4, 'max': 1800},
        'dnssl_lifetime': {'min': 1, 'max': 4294967295},
        'link_mtu': {'min': 1280, 'max': 65535},
        'preferred_lifetime': {'min': 1, 'max': 4294967295},
        'rdnss_lifetime': {'min': 1, 'max': 4294967295},
        'route_lifetime': {'min': 1, 'max': 4294967295},
        'valid_lifetime': {'min': 1, 'max': 4294967295},
        'hop_limit': {'min': 0, 'max': 255},
    }
    EXIST_ATTR = 'entry'

    def __init__(self, module: AnsibleModule, result: dict, session: Session = None, fail: dict = None):
        BaseModule.__init__(self=self, m=module, r=result, s=session, f=fail)
        self.entry = {}

    def _simplify_existing(self, entry: dict) -> dict:
        simple = simplify_translate(
            existing=entry,
            typing=self.FIELDS_TYPING,
            translate=self.FIELDS_TRANSLATE,
        )

        for field in ['routes', 'rdnss', 'dnssl']:
            simple[field] = get_selected_list(simple[field], remove_empty=True)

        return simple
