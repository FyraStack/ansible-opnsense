#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.handler import \
    module_dependency_error, MODULE_EXCEPTIONS

try:
    from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.api import Session
    from ansible_collections.fyrastack.opnsense.plugins.module_utils.defaults.main import \
        OPN_MOD_ARGS, RELOAD_MOD_ARG, STATE_ONLY_MOD_ARG

except MODULE_EXCEPTIONS:
    module_dependency_error()


def _api_cnf(command, data=None, params=None):
    return {
        'module': 'kea',
        'controller': 'dhcpv6',
        'command': command,
        'data': data,
        'params': params,
    }


def _search_rows(session, command):
    return session.post(_api_cnf(
        command=command,
        data={'current': 1, 'rowCount': 1000},
    )).get('rows', [])


def _find_subnet_uuid(module, session, subnet):
    for row in _search_rows(session, 'search_subnet'):
        if row.get('subnet') == subnet:
            return row['uuid']

    if module.check_mode:
        return None

    module.fail_json(msg=f"DHCPv6 subnet '{subnet}' was not found")


def _pool_subnet_matches(pool, subnet, subnet_uuid):
    return (
        pool.get('subnet') == subnet_uuid or
        pool.get('subnet') == subnet or
        pool.get('%subnet') == subnet or
        str(pool.get('%subnet', '')).endswith(f" {subnet}")
    )


def _normalize_pool(pool, subnet, subnet_uuid):
    return {
        'subnet': subnet,
        'subnet_uuid': subnet_uuid,
        'prefix': pool.get('prefix', ''),
        'prefix_len': int(pool['prefix_len']) if str(pool.get('prefix_len', '')).isdigit() else pool.get('prefix_len', ''),
        'delegated_len': int(pool['delegated_len']) if str(pool.get('delegated_len', '')).isdigit() else pool.get('delegated_len', ''),
        'description': pool.get('description', ''),
    }


def _desired(params, subnet_uuid):
    return {
        'subnet': params['subnet'],
        'subnet_uuid': subnet_uuid,
        'prefix': params['prefix'],
        'prefix_len': params['prefix_len'],
        'delegated_len': params['delegated_len'],
        'description': params['description'],
    }


def _request(params, subnet_uuid):
    return {
        'pd_pool': {
            'subnet': subnet_uuid,
            'prefix': params['prefix'],
            'prefix_len': str(params['prefix_len']),
            'delegated_len': str(params['delegated_len']),
            'description': params['description'],
        }
    }


def _matches(pool, params, subnet_uuid):
    if not _pool_subnet_matches(pool, params['subnet'], subnet_uuid):
        return False

    for field in params['match_fields']:
        if field == 'subnet':
            continue

        if str(pool.get(field, '')) != str(params[field]):
            return False

    return True


def run_module():
    module_args = dict(
        subnet=dict(type='str', required=True),
        prefix=dict(type='str', required=True),
        prefix_len=dict(type='int', required=True),
        delegated_len=dict(type='int', required=False, default=64),
        description=dict(type='str', required=False, default='', aliases=['desc']),
        match_fields=dict(
            type='list', elements='str', required=False,
            choices=['subnet', 'prefix', 'prefix_len', 'delegated_len', 'description'],
            default=['subnet', 'prefix', 'prefix_len', 'delegated_len'],
        ),
        **RELOAD_MOD_ARG,
        **STATE_ONLY_MOD_ARG,
        **OPN_MOD_ARGS,
    )

    result = dict(
        changed=False,
        diff={
            'before': {},
            'after': {},
        },
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    params = module.params

    with Session(module=module) as session:
        subnet_uuid = _find_subnet_uuid(module, session, params['subnet'])
        desired = _desired(params, subnet_uuid)

        existing = None
        for pool in _search_rows(session, 'search_pd_pool'):
            if _matches(pool, params, subnet_uuid):
                existing = pool
                break

        if params['state'] == 'absent':
            if existing is not None:
                result['changed'] = True
                result['diff']['before'] = _normalize_pool(existing, params['subnet'], subnet_uuid)
                result['diff']['after'] = {}
                if not module.check_mode:
                    session.post(_api_cnf('del_pd_pool', params=[existing['uuid']]))
            else:
                result['diff'] = {}

        elif existing is None:
            result['changed'] = True
            result['diff']['before'] = {}
            result['diff']['after'] = desired
            if not module.check_mode:
                session.post(_api_cnf('add_pd_pool', data=_request(params, subnet_uuid)))

        else:
            before = _normalize_pool(existing, params['subnet'], subnet_uuid)
            result['diff']['before'] = before
            result['diff']['after'] = desired
            for field in ['prefix', 'prefix_len', 'delegated_len', 'description']:
                if str(before[field]) != str(desired[field]):
                    result['changed'] = True
                    break

            if result['changed'] and not module.check_mode:
                session.post(_api_cnf('set_pd_pool', data=_request(params, subnet_uuid), params=[existing['uuid']]))

        if result['changed'] and params['reload'] and not module.check_mode:
            session.post(_api_cnf('reconfigure').copy() | {'controller': 'service'})

    if not result['changed']:
        result['diff'] = {}

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
