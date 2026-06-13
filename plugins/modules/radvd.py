#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.handler import \
    module_dependency_error, MODULE_EXCEPTIONS

try:
    from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.wrapper import module_wrapper
    from ansible_collections.fyrastack.opnsense.plugins.module_utils.defaults.main import \
        OPN_MOD_ARGS, STATE_MOD_ARG, RELOAD_MOD_ARG
    from ansible_collections.fyrastack.opnsense.plugins.module_utils.main.radvd import Radvd

except MODULE_EXCEPTIONS:
    module_dependency_error()


def run_module():
    module_args = dict(
        interface=dict(type='str', required=True),
        mode=dict(
            type='str', required=False, default='stateless',
            choices=['router', 'unmanaged', 'managed', 'assist', 'stateless'],
        ),
        base6_interface=dict(type='str', required=False, default=''),
        deprecate_prefix=dict(type='str', required=False, default='', choices=['', 'on', 'off']),
        remove_adv_on_exit=dict(type='str', required=False, default='', choices=['', 'on', 'off']),
        remove_route=dict(type='str', required=False, default='', choices=['', 'on', 'off']),
        routes=dict(type='list', elements='str', required=False, default=[]),
        rdnss=dict(type='list', elements='str', required=False, default=[]),
        dnssl=dict(type='list', elements='str', required=False, default=[]),
        dns=dict(type='bool', required=False, default=True),
        min_interval=dict(type='int', required=False, default=200),
        max_interval=dict(type='int', required=False, default=600),
        dnssl_lifetime=dict(type='int', required=False),
        default_lifetime=dict(type='int', required=False),
        link_mtu=dict(type='int', required=False),
        preferred_lifetime=dict(type='int', required=False),
        ra_src_address=dict(type='str', required=False, default=''),
        rdnss_lifetime=dict(type='int', required=False),
        route_lifetime=dict(type='int', required=False),
        valid_lifetime=dict(type='int', required=False),
        default_preference=dict(
            type='str', required=False, default='medium',
            choices=['low', 'medium', 'high'],
        ),
        nat64prefix=dict(type='str', required=False, default=''),
        hop_limit=dict(type='int', required=False, default=64),
        match_fields=dict(
            type='list', required=False, elements='str',
            choices=['interface'],
            default=['interface'],
        ),
        **RELOAD_MOD_ARG,
        **STATE_MOD_ARG,
        **OPN_MOD_ARGS,
    )

    result = dict(
        changed=False,
        diff={
            'before': {},
            'after': {},
        }
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    module_wrapper(Radvd(module=module, result=result))
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
