#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (C) 2026, Fyra Stack
# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.handler import \
    module_dependency_error, MODULE_EXCEPTIONS

try:
    from ansible_collections.fyrastack.opnsense.plugins.module_utils.base.api import Session
    from ansible_collections.fyrastack.opnsense.plugins.module_utils.defaults.main import \
        OPN_MOD_ARGS, STATE_ONLY_MOD_ARG

except MODULE_EXCEPTIONS:
    module_dependency_error()


DOCUMENTATION = r'''
---
module: interface_assignment
short_description: Manage OPNsense interface assignments
description:
  - Manage OPNsense interface assignments through the patched assign_settings API controller.
  - The module is intentionally strict and refuses to silently reuse a different assignment name when a device or description already exists elsewhere.
options:
  name:
    description:
      - OPNsense assignment name, for example C(opt1040).
    required: true
    type: str
    aliases: [assignment, interface, ifname]
  device:
    description:
      - Physical or virtual device to assign, for example C(vlan0.1040).
    required: false
    type: str
  description:
    description:
      - Interface description shown in OPNsense.
    required: false
    type: str
    aliases: [descr, desc]
  enabled:
    description:
      - Whether the assigned interface should be enabled.
    required: false
    type: bool
    aliases: [enable]
  ipaddr:
    description:
      - IPv4 address to configure on the interface.
    required: false
    type: str
    aliases: [ip, address]
  subnet:
    description:
      - IPv4 prefix length to configure on the interface.
    required: false
    type: int
    aliases: [prefix, cidr]
  ipaddrv6:
    description:
      - IPv6 address to configure on the interface.
    required: false
    type: str
    aliases: [ip6, ipv6, address6]
  subnetv6:
    description:
      - IPv6 prefix length to configure on the interface.
    required: false
    type: int
    aliases: [prefix6, cidr6]
  spoofmac:
    description:
      - Spoofed MAC address.
    required: false
    type: str
    default: ''
  gateway_interface:
    description:
      - Whether this assignment should be treated as a gateway interface.
    required: false
    type: bool
  match_by:
    description:
      - Ordered fields used to find an existing assignment before configuring it.
      - The default C([name]) keeps assignment names strict and avoids accidental adoption.
      - Description matches are only adopted when the current assignment device also matches C(device).
      - Use C([description, name]) when adopting already-existing assignments with known descriptions.
    required: false
    type: list
    elements: str
    choices: [name, description, device]
    default: [name]
  state:
    description:
      - Whether the assignment should exist.
    required: false
    type: str
    choices: [present, absent]
    default: present
author:
  - Fyra Stack
'''

EXAMPLES = r'''
- name: Assign VLAN 1040 to opt1040
  fyrastack.opnsense.interface_assignment:
    name: opt1040
    device: vlan0.1040
    description: publicvm
    enabled: true

- name: Assign VLAN 3033 with an IPv4 address
  fyrastack.opnsense.interface_assignment:
    name: opt33
    device: vlan0.3033
    description: COLO_33
    ipaddr: 144.225.81.129
    subnet: 29

- name: Assign WAN with IPv4 and IPv6 addresses
  fyrastack.opnsense.interface_assignment:
    name: opt10
    device: ixl0
    description: WAN_HE
    ipaddr: 184.105.54.114
    subnet: 29
    ipaddrv6: 2001:470:496:1::2
    subnetv6: 124

- name: Adopt an already-existing assignment by description
  fyrastack.opnsense.interface_assignment:
    name: opt1040
    match_by:
      - description
      - name
    device: vlan0.1040
    description: publicvm
'''

RETURN = r'''
assignment_name:
  description: OPNsense assignment name managed by this module.
  returned: always
  type: str
matched_by:
  description: Field that matched the existing assignment.
  returned: always
  type: str
requested_name:
  description: Assignment name requested by the user.
  returned: always
  type: str
assignment:
  description: Assignment details returned by OPNsense after changes.
  returned: always
  type: dict
conflicts:
  description: Existing conflicting assignment names, when detected.
  returned: failure
  type: dict
'''


ASSIGN_API = dict(
    module='interfaces',
    controller='assign_settings',
)


def _is_opt_assignment(name):
    return name.startswith('opt') and name[3:].isdigit()


def _assign_cnf(command, params=None, data=None):
    cnf = dict(ASSIGN_API)
    cnf['command'] = command
    if params is not None:
        cnf['params'] = params
    if data is not None:
        cnf['data'] = data
    return cnf


def _as_str(value):
    if value is None:
        return None
    return str(value)


def _enabled(value):
    return value is True or value == '1' or value == 1 or value == 'true'


def _get_interfaces(session):
    response = session.get(_assign_cnf('get_interface_list'))
    return response.get('interfaces', {})


def _get_assignment(session, name):
    response = session.get(_assign_cnf('get_item', params=[name]))
    assignment = response.get('assign', {})
    if not isinstance(assignment, dict):
        return {}
    return assignment


def _find_by_field(interfaces, field, value):
    if value is None:
        return []
    return [
        name for name, entry in interfaces.items()
        if _as_str(entry.get(field)) == _as_str(value)
    ]


def _is_compatible_match(entry, field, params):
    if field == 'description' and params['device'] is not None:
        return _as_str(entry.get('device')) == _as_str(params['device'])

    return True


def _resolve_assignment(module, requested_name, interfaces, params):
    field_map = {
        'description': 'descr',
        'device': 'device',
    }

    for field in params['match_by']:
        if field == 'name':
            if requested_name in interfaces:
                return requested_name, 'name'
            continue

        value = params[field]
        raw_matches = _find_by_field(interfaces, field_map[field], value)
        matches = [
            match for match in raw_matches
            if _is_compatible_match(interfaces[match], field, params)
        ]

        if len(raw_matches) > 0 and len(matches) == 0:
            continue

        if len(matches) > 1:
            module.fail_json(
                msg=f"Multiple interface assignments match {field}={value}: {matches}",
                matches=matches,
                match_by=field,
            )

        if len(matches) == 1:
            return matches[0], field

    return requested_name, None


def _refresh_assignment(session, name):
    interfaces = _get_interfaces(session)
    return interfaces, interfaces.get(name, {})


def _desired_payload(params):
    payload = {
        'device': params['device'],
        'descr': params['description'],
        'spoofmac': params['spoofmac'] or '',
    }

    optional_fields = (
        'enabled',
        'ipaddr',
        'subnet',
        'ipaddrv6',
        'subnetv6',
        'gateway_interface',
    )
    for field in optional_fields:
        if params[field] is not None:
            payload['enable' if field == 'enabled' else field] = params[field]

    return payload


def _apply_assignment(session, name, payload):
    if _is_opt_assignment(name):
        return session.post(_assign_cnf(
            command='set_item',
            params=[name],
            data={'assign': payload},
        ))

    payload = dict(payload)
    payload['interface'] = name
    return session.post(_assign_cnf(
        command='add_item',
        data={'assign': payload},
    ))


def _entry_changed(entry, detail, payload, params):
    if not isinstance(entry, dict):
        return True

    comparisons = {
        'device': ('device', payload.get('device')),
        'descr': ('descr', payload.get('descr')),
        'ipaddr': ('ipaddr', payload.get('ipaddr')),
        'subnet': ('subnet', payload.get('subnet')),
        'ipaddrv6': ('ipaddrv6', payload.get('ipaddrv6')),
        'subnetv6': ('subnetv6', payload.get('subnetv6')),
    }
    for entry_field, (_, desired) in comparisons.items():
        if desired is not None and _as_str(entry.get(entry_field)) != _as_str(desired):
            return True

    if params['enabled'] is not None and detail:
        if _enabled(detail.get('enable')) != params['enabled']:
            return True

    if params['gateway_interface'] is not None and detail:
        if _enabled(detail.get('gateway_interface')) != params['gateway_interface']:
            return True

    return False


def _validate_current_state(module, name, entry, payload):
    mismatches = {}
    for field, desired in (
        ('device', payload.get('device')),
        ('descr', payload.get('descr')),
        ('ipaddr', payload.get('ipaddr')),
        ('subnet', payload.get('subnet')),
        ('ipaddrv6', payload.get('ipaddrv6')),
        ('subnetv6', payload.get('subnetv6')),
    ):
        if desired is not None and _as_str(entry.get(field)) != _as_str(desired):
            mismatches[field] = {
                'expected': _as_str(desired),
                'actual': _as_str(entry.get(field)),
            }

    if len(mismatches) > 0:
        module.fail_json(
            msg=f"Interface assignment {name} did not reconcile to the requested state",
            assignment=name,
            mismatches=mismatches,
        )


def _validate_conflicts(module, name, interfaces, payload, ignore_names=None):
    ignore_names = set(ignore_names or [])
    ignore_names.add(name)

    conflicts = {}
    for field, value in (('device', payload.get('device')), ('descr', payload.get('descr'))):
        matches = [match for match in _find_by_field(interfaces, field, value) if match not in ignore_names]
        if len(matches) > 0:
            conflicts[field] = matches

    if len(conflicts) > 0:
        module.fail_json(
            msg=(
                f"Refusing to assign {payload['device']} to {name}: matching assignment(s) "
                f"already exist on other interface name(s): {conflicts}. "
                "Unassign or rename the conflicting interface first."
            ),
            conflicts=conflicts,
            assignment=name,
            device=payload['device'],
        )


def run_module():
    module_args = dict(
        name=dict(
            type='str', required=True, aliases=['assignment', 'interface', 'ifname'],
            description='OPNsense assignment name, for example opt1040.',
        ),
        device=dict(
            type='str', required=False,
            description='Physical or virtual device to assign, for example vlan0.1040.',
        ),
        description=dict(type='str', required=False, aliases=['descr', 'desc']),
        enabled=dict(type='bool', required=False, aliases=['enable']),
        ipaddr=dict(type='str', required=False, aliases=['ip', 'address']),
        subnet=dict(type='int', required=False, aliases=['prefix', 'cidr']),
        ipaddrv6=dict(type='str', required=False, aliases=['ip6', 'ipv6', 'address6']),
        subnetv6=dict(type='int', required=False, aliases=['prefix6', 'cidr6']),
        spoofmac=dict(type='str', required=False, default='', no_log=False),
        gateway_interface=dict(type='bool', required=False),
        match_by=dict(
            type='list',
            elements='str',
            required=False,
            default=['name'],
            choices=['name', 'description', 'device'],
        ),
        **STATE_ONLY_MOD_ARG,
        **OPN_MOD_ARGS,
    )

    result = dict(
        changed=False,
        assignment={},
        assignment_name=None,
        requested_name=None,
        matched_by=None,
        conflicts={},
        diff={
            'before': {},
            'after': {},
        },
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[
            ('state', 'present', ('device', 'description')),
        ],
    )

    params = module.params
    requested_name = params['name']
    result['requested_name'] = requested_name

    with Session(module=module) as session:
        # Always list first. The list response is our source of truth for
        # selecting which assignment name this run is allowed to reconcile.
        interfaces = _get_interfaces(session)
        name, matched_by = _resolve_assignment(
            module=module,
            requested_name=requested_name,
            interfaces=interfaces,
            params=params,
        )
        result['assignment_name'] = name
        result['matched_by'] = matched_by

        existing_entry = interfaces.get(name, {})
        existing_detail = _get_assignment(session, name) if name in interfaces else {}

        if params['state'] == 'absent':
            if name not in interfaces:
                module.exit_json(**result)

            result['changed'] = True
            result['diff']['before'] = existing_entry
            if not module.check_mode:
                response = session.post(_assign_cnf('del_item', params=[name]))
                if response.get('result') != 'deleted':
                    module.fail_json(msg=f"Failed to delete interface assignment {name}", response=response)
                interfaces, existing_entry = _refresh_assignment(session, name)
                if name in interfaces:
                    module.fail_json(
                        msg=f"Interface assignment {name} still exists after delete",
                        assignment=name,
                        current=existing_entry,
                    )
            module.exit_json(**result)

        payload = _desired_payload(params)
        target_name = requested_name
        rename_assignment = (
            name != requested_name and
            matched_by in ('description', 'device') and
            requested_name not in interfaces
        )

        if name != requested_name and requested_name in interfaces:
            module.fail_json(
                msg=(
                    f"Refusing to rename interface assignment {name} to {requested_name}: "
                    f"{requested_name} already exists."
                ),
                assignment=name,
                requested_name=requested_name,
                existing=interfaces[requested_name],
            )

        # Refuse to apply if the desired identity already exists on another
        # assignment name. This prevents set_item from accidentally mutating
        # opt3/optN when the caller asked to reconcile a different assignment.
        _validate_conflicts(
            module=module,
            name=name,
            interfaces=interfaces,
            payload=payload,
            ignore_names=[name] if rename_assignment else None,
        )

        changed = _entry_changed(
            entry=existing_entry,
            detail=existing_detail,
            payload=payload,
            params=params,
        ) or rename_assignment

        result['changed'] = changed
        result['assignment_name'] = target_name if rename_assignment else name
        result['assignment'] = existing_entry
        result['diff']['before'] = existing_entry
        result['diff']['after'] = payload

        if changed and not module.check_mode:
            if rename_assignment:
                response = session.post(_assign_cnf('del_item', params=[name]))
                if response.get('result') != 'deleted':
                    module.fail_json(
                        msg=f"Failed to delete old interface assignment {name} while renaming to {target_name}",
                        response=response,
                        assignment=name,
                        requested_name=target_name,
                    )

            response = _apply_assignment(session=session, name=target_name, payload=payload)
            if response.get('result') != 'saved':
                module.fail_json(
                    msg=f"Failed to configure interface assignment {target_name}",
                    response=response,
                    assignment=target_name,
                    payload=payload,
                )

            interfaces, reconciled_entry = _refresh_assignment(session, target_name)
            if target_name not in interfaces:
                module.fail_json(
                    msg=f"Interface assignment {target_name} was not returned after applying changes",
                    assignment=target_name,
                    payload=payload,
                )
            _validate_current_state(
                module=module,
                name=target_name,
                entry=reconciled_entry,
                payload=payload,
            )
            result['assignment'] = reconciled_entry

        module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
