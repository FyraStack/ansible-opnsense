from ansible.module_utils.basic import AnsibleModule

from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.api import \
    Session
from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.cls import GeneralModule


class GeneralV6(GeneralModule):
    CMDS = {
        'set': 'set',
        'search': 'get'
    }
    API_KEY_PATH = 'dhcpv6.general'
    API_KEY_PATH_REQ = API_KEY_PATH
    API_MOD = 'kea'
    API_CONT = 'dhcpv6'
    API_CONT_REL = 'service'
    FIELDS_CHANGE = [
        'enabled', 'interfaces', 'fw_rules', 'lifetime'
    ]
    FIELDS_ALL = FIELDS_CHANGE
    FIELDS_TRANSLATE = {
        'lifetime': 'valid_lifetime',
        'fw_rules': 'fwrules',
    }
    FIELDS_TYPING = {
        'bool': ['enabled', 'fw_rules'],
        'int': ['lifetime'],
        'list': ['interfaces'],
    }
    INT_VALIDATIONS = {
        'lifetime': {'min': 0},
    }

    def __init__(self, module: AnsibleModule, result: dict, session: Session = None):
        GeneralModule.__init__(self=self, m=module, r=result, s=session)
