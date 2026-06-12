# Ansible Collection to manage OPNsense Firewalls

<p align="center">
    <a title="Support this Project (Donate, Support-Licenses)" href="https://shop.oxl.app/collections/open-source">
        <img src="https://files.oxl.at/img/badge-oss-support.svg" alt="Support Badge (Donate, Support-Licenses)"/>
    </a>
</p>

----

[![Lint Python](https://github.com/O-X-L/ansible-opnsense/actions/workflows/lint-python.yml/badge.svg)](https://github.com/O-X-L/ansible-opnsense/actions/workflows/lint-python.yml)
[![Lint Ansible](https://github.com/O-X-L/ansible-opnsense/actions/workflows/lint-ansible.yml/badge.svg)](https://github.com/O-X-L/ansible-opnsense/actions/workflows/lint-ansible.yml)
[![Unit Test Status](https://github.com/O-X-L/ansible-opnsense/actions/workflows/unit_test.yml/badge.svg)](https://github.com/O-X-L/ansible-opnsense/actions/workflows/unit_test.yml)
[![Ansible Galaxy](https://badges.oss.oxl.app/galaxy.badge.svg)](https://galaxy.ansible.com/ui/repo/published/oxlorg/opnsense)

**Functional Tests**: 

* Status: [![Functional Test Status](https://badges.oss.oxl.app/fyrastack.opnsense.collection.test.svg)](https://github.com/O-X-L/ansible-opnsense/actions/workflows/functional_test_result.yml) |
[![Functional-Tests](https://github.com/O-X-L/ansible-opnsense/actions/workflows/functional_test_result.yml/badge.svg)](https://github.com/O-X-L/ansible-opnsense/actions/workflows/functional_test_result.yml)
* Logs: [API](https://ci.oss.oxl.app/api/job/ansible-test-collection-opnsense/logs?token=2b7bba30-9a37-4b57-be8a-99e23016ce70&lines=1000) |
[Daily Archive](https://github.com/O-X-L/ansible-opnsense/actions/workflows/functional_test_result.yml)

Internal CI: [Tester Role](https://github.com/O-X-L/ansible-role-oxl-cicd) | [Jobs API](https://github.com/O-X-L/github-self-hosted-jobs-systemd)

----

## Requirements

The [httpx python module](https://www.python-httpx.org/) is used for API communications!

```bash
python3 -m pip install --upgrade httpx
```

Then - install the collection itself:

```bash
# latest version:
ansible-galaxy collection install git+https://github.com/O-X-L/ansible-opnsense.git

# stable/tested version:
ansible-galaxy collection install git+https://github.com/O-X-L/ansible-opnsense.git,25.7.8
## OR
ansible-galaxy collection install fyrastack.opnsense
```

----

## Usage

See: [Docs](https://ansible-opnsense.oxl.app)

[![Docs Uptime](https://status.oxl.at/api/v1/endpoints/1--oxl_opnsense-ansible-collection-docs/uptimes/7d/badge.svg)](https://status.oxl.at/endpoints/1--oxl_opnsense-ansible-collection-docs)

If you DO NOT want to use Ansible - [this fork](https://github.com/O-X-L/opnsense-api-client) provides you with a raw Python3 interface.

----

## Support the project(s)

Support the Open-Source projects that make these modules possible:

* [Donate to OPNsense](https://opnsense.org/donate/) or [Buy the Business-Edition](https://shop.opnsense.com/product-categorie/software_and_licenses/)
* [Donate to the Ansible-Module Maintainers](https://shop.oxl.app/products/open-source-spende) or [Buy a Support-License](https://shop.oxl.app/products/open-source-support-opnsense-ansible-collection)

----

## Contribute

Feel free to contribute to this project using [pull-requests](https://github.com/O-X-L/ansible-opnsense/pulls), [issues](https://github.com/O-X-L/ansible-opnsense/issues) and [discussions](https://github.com/O-X-L/ansible-opnsense/discussions)!

See also: [Contributing](https://github.com/O-X-L/ansible-opnsense/blob/latest/CONTRIBUTING.md)

<img src="https://contrib.rocks/image?repo=O-X-L/ansible-opnsense&max=7" />

----

## Version Support

We try that the `fyrastack.opnsense` modules always support the latest version of OPNsense.

If an API changed, the current module-implementation might fail for firewalls running an older firmware.

As [this project is unfunded](https://github.com/O-X-L/ansible-opnsense/discussions/199) we do not actively check for API-changes - if you find missing functionalities you need/want to have please [report it](https://github.com/O-X-L/ansible-opnsense/issues)!

----


## Modules

**Development States**:

not implemented => development => [testing](https://github.com/O-X-L/ansible-opnsense/tree/latest/tests) => [unstable (_practical testing_)](https://github.com/O-X-L/ansible-opnsense/discussions/85) => stable

### Implemented


| Function                  | Module                                                         | Usage                                                                                                           | State    |
|:--------------------------|:---------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|:---------|
| **Base**                  | fyrastack.opnsense.list                                           | [Docs](https://ansible-opnsense.oxl.app/general/list.html)                                                      | stable   |
| **Base**                  | fyrastack.opnsense.reload                                         | [Docs](https://ansible-opnsense.oxl.app/general/reload.html)                                                    | stable   |
| **Raw**                   | fyrastack.opnsense.raw                                            | [Docs](https://ansible-opnsense.oxl.app/general/raw.html)                                                       | unstable |
| **Services**              | fyrastack.opnsense.service                                        | [Docs](https://ansible-opnsense.oxl.app/general/service.html)                                                   | stable   |
| **Alias**                 | fyrastack.opnsense.alias                                          | [Docs](https://ansible-opnsense.oxl.app/modules/alias.html)                                                     | stable   | 
| **Alias**                 | fyrastack.opnsense.alias_multi                                    | [Docs](https://ansible-opnsense.oxl.app/modules/alias_multi.html)                                               | stable   |
| **Alias**                 | fyrastack.opnsense.alias_purge                                    | [Docs](https://ansible-opnsense.oxl.app/modules/alias_multi.html#oxlorg-opnsense-alias-purge)                   | unstable |
| **Rules**                 | fyrastack.opnsense.rule                                           | [Docs](https://ansible-opnsense.oxl.app/modules/rule.html)                                                      | stable   |
| **Rules**                 | fyrastack.opnsense.rule_multi                                     | [Docs](https://ansible-opnsense.oxl.app/modules/rule_multi.html)                                                | stable   |
| **Rules**                 | fyrastack.opnsense.rule_purge                                     | [Docs](https://ansible-opnsense.oxl.app/modules/rule_multi.html#oxlorg-opnsense-rule-purge)                     | unstable |
| **Rule Interface Groups** | fyrastack.opnsense.rule_interface_group                           | [Docs](https://ansible-opnsense.oxl.app/modules/rule_interface_group.html#oxlorg-opnsense-rule-interface-group) | stable |
| **Savepoints**            | fyrastack.opnsense.savepoint                                      | [Docs](https://ansible-opnsense.oxl.app/modules/savepoint.html)                                                 | stable   |
| **Packages**              | fyrastack.opnsense.package                                        | [Docs](https://ansible-opnsense.oxl.app/modules/package.html)                                                   | stable   |
| **System**                | fyrastack.opnsense.system                                         | [Docs](https://ansible-opnsense.oxl.app/modules/system.html)                                                    | stable   |
| **Cron-Jobs**             | fyrastack.opnsense.cron                                           | [Docs](https://ansible-opnsense.oxl.app/modules/cron.html)                                                      | stable   |
| **Routes**                | fyrastack.opnsense.route                                          | [Docs](https://ansible-opnsense.oxl.app/modules/routing.html)                                                   | stable   |
| **Gateways**              | fyrastack.opnsense.gateway                                        | [Docs](https://ansible-opnsense.oxl.app/modules/routing.html)                                                   | stable |
| **DNS**                   | fyrastack.opnsense.unbound_general                                | [Docs](https://ansible-opnsense.oxl.app/modules/unbound_general.html)                                           | stable   |
| **DNS**                   | fyrastack.opnsense.unbound_acl                                    | [Docs](https://ansible-opnsense.oxl.app/modules/unbound_acl.html)                                               | stable   |
| **DNS**                   | fyrastack.opnsense.unbound_forward                                | [Docs](https://ansible-opnsense.oxl.app/modules/unbound_forwarding.html)                                        | stable   |
| **DNS**                   | fyrastack.opnsense.unbound_dot                                    | [Docs](https://ansible-opnsense.oxl.app/modules/unbound_dot.html)                                               | stable   |
| **DNS**                   | fyrastack.opnsense.unbound_host                                   | [Docs](https://ansible-opnsense.oxl.app/modules/unbound_host.html)                                              | stable   |
| **DNS**                   | fyrastack.opnsense.unbound_host_alias                             | [Docs](https://ansible-opnsense.oxl.app/modules/unbound_host_alias.html)                                        | stable   |
| **DNS**                   | fyrastack.opnsense.unbound_dnsbl                                  | [Docs](https://ansible-opnsense.oxl.app/modules/unbound_host_alias.html)                                        | stable |
| **Syslog**                | fyrastack.opnsense.syslog                                         | [Docs](https://ansible-opnsense.oxl.app/modules/syslog.html)                                                    | stable   |
| **IPSec**                 | fyrastack.opnsense.ipsec_connection, fyrastack.opnsense.ipsec_tunnel | [Docs](https://ansible-opnsense.oxl.app/modules/ipsec.html)                                                     | stable   |
| **IPSec**                 | fyrastack.opnsense.ipsec_pool, fyrastack.opnsense.ipsec_network      | [Docs](https://ansible-opnsense.oxl.app/modules/ipsec.html)                                                     | stable   |
| **IPSec**                 | fyrastack.opnsense.ipsec_auth_local                               | [Docs](https://ansible-opnsense.oxl.app/modules/ipsec.html)                                                     | stable   |
| **IPSec**                 | fyrastack.opnsense.ipsec_auth_remote                              | [Docs](https://ansible-opnsense.oxl.app/modules/ipsec.html)                                                     | stable   |
| **IPSec**                 | fyrastack.opnsense.ipsec_child                                    | [Docs](https://ansible-opnsense.oxl.app/modules/ipsec.html)                                                     | stable   |
| **IPSec**                 | fyrastack.opnsense.ipsec_vti                                      | [Docs](https://ansible-opnsense.oxl.app/modules/ipsec.html)                                                     | stable   |
| **IPSec**                 | fyrastack.opnsense.ipsec_cert                                     | [Docs](https://ansible-opnsense.oxl.app/modules/ipsec.html)                                                     | stable   |
| **IPSec**                 | fyrastack.opnsense.ipsec_psk                                      | [Docs](https://ansible-opnsense.oxl.app/modules/ipsec.html)                                                     | stable   |
| **IPSec**                 | fyrastack.opnsense.ipsec_manual_spd                               | [Docs](https://ansible-opnsense.oxl.app/modules/ipsec.html)                                                     | stable   |
| **IPSec**                 | fyrastack.opnsense.general                                        | [Docs](https://ansible-opnsense.oxl.app/modules/ipsec.html)                                                     | unstable |
| **Traffic Shaper**        | fyrastack.opnsense.shaper_pipe                                    | [Docs](https://ansible-opnsense.oxl.app/modules/shaper.html)                                                    | stable   |
| **Traffic Shaper**        | fyrastack.opnsense.shaper_queue                                   | [Docs](https://ansible-opnsense.oxl.app/modules/shaper.html)                                                    | stable   |
| **Traffic Shaper**        | fyrastack.opnsense.shaper_rule                                    | [Docs](https://ansible-opnsense.oxl.app/modules/shaper.html)                                                    | stable   |
| **Monit**                 | fyrastack.opnsense.monit_service                                  | [Docs](https://ansible-opnsense.oxl.app/modules/monit.html)                                                     | stable   |
| **Monit**                 | fyrastack.opnsense.monit_alert                                    | [Docs](https://ansible-opnsense.oxl.app/modules/monit.html)                                                     | stable   |
| **Monit**                 | fyrastack.opnsense.monit_test                                     | [Docs](https://ansible-opnsense.oxl.app/modules/monit.html)                                                     | stable   |
| **WireGuard**             | fyrastack.opnsense.wireguard_server                               | [Docs](https://ansible-opnsense.oxl.app/modules/wireguard.html)                                                 | stable   |
| **WireGuard**             | fyrastack.opnsense.wireguard_peer                                 | [Docs](https://ansible-opnsense.oxl.app/modules/wireguard.html)                                                 | stable   |
| **WireGuard**             | fyrastack.opnsense.wireguard_show                                 | [Docs](https://ansible-opnsense.oxl.app/modules/wireguard.html)                                                 | stable   |
| **WireGuard**             | fyrastack.opnsense.wireguard_general                              | [Docs](https://ansible-opnsense.oxl.app/modules/wireguard.html)                                                 | stable   |
| **Interfaces**            | fyrastack.opnsense.interface_vlan                                 | [Docs](https://ansible-opnsense.oxl.app/modules/interface.html)                                                 | stable   |
| **Interfaces**            | fyrastack.opnsense.interface_vxlan                                | [Docs](https://ansible-opnsense.oxl.app/modules/interface.html)                                                 | stable   |
| **Interfaces**            | fyrastack.opnsense.interface_vip                                  | [Docs](https://ansible-opnsense.oxl.app/modules/interface.html)                                                 | stable   |
| **Interfaces**            | fyrastack.opnsense.interface_lagg                                 | [Docs](https://ansible-opnsense.oxl.app/modules/interface.html)                                                 | stable |
| **Interfaces**            | fyrastack.opnsense.interface_loopback                             | [Docs](https://ansible-opnsense.oxl.app/modules/interface.html)                                                 | stable |
| **Interfaces**            | fyrastack.opnsense.interface_gre                                  | [Docs](https://ansible-opnsense.oxl.app/modules/interface.html)                                                 | stable   |
| **Interfaces**            | fyrastack.opnsense.interface_bridge                               | [Docs](https://ansible-opnsense.oxl.app/modules/interface.html)                                                 | unstable |
| **Interfaces**            | fyrastack.opnsense.interface_gif                                  | [Docs](https://ansible-opnsense.oxl.app/modules/interface.html)                                                 | unstable |
| **NAT**                   | fyrastack.opnsense.nat_source                                     | [Docs](https://ansible-opnsense.oxl.app/modules/source_nat.html)                                                | stable   |
| **NAT**                   | fyrastack.opnsense.nat_one_to_one                                 | [Docs](https://ansible-opnsense.oxl.app/modules/one_to_one.html)                                                | stable |
| **Dynamic Routing**       | fyrastack.opnsense.frr_diagnostic                                 | [Docs](https://ansible-opnsense.oxl.app/modules/frr_diagnostic.html)                                            | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_general                                    | [Docs](https://ansible-opnsense.oxl.app/modules/frr_general.html)                                               | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_bfd_general                                | [Docs](https://ansible-opnsense.oxl.app/modules/frr_bfd.html#oxlorg-opnsense-frr-bfd-general)                   | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_bfd_neighbor                               | [Docs](https://ansible-opnsense.oxl.app/modules/frr_bfd.html#oxlorg-opnsense-frr-bfd-neighbor)                  | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_bgp_general                                | [Docs](https://ansible-opnsense.oxl.app/modules/frr_bgp.html#oxlorg-opnsense-frr-bgp-general)                   | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_bgp_neighbor                               | [Docs](https://ansible-opnsense.oxl.app/modules/frr_bgp.html#oxlorg-opnsense-frr-bgp-neighbor)                  | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_bgp_prefix_list                            | [Docs](https://ansible-opnsense.oxl.app/modules/frr_bgp.html#oxlorg-opnsense-frr-bgp-prefix-list)               | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_bgp_route_map                              | [Docs](https://ansible-opnsense.oxl.app/modules/frr_bgp.html#oxlorg-opnsense-frr-bgp-route-map)                 | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_bgp_community_list                         | [Docs](https://ansible-opnsense.oxl.app/modules/frr_bgp.html#oxlorg-opnsense-frr-bgp-community-list)            | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_bgp_as_path                                | [Docs](https://ansible-opnsense.oxl.app/modules/frr_bgp.html#oxlorg-opnsense-frr-bgp-as-path)                   | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_bgp_redistribution                         | [Docs](https://ansible-opnsense.oxl.app/modules/frr_bgp.html#oxlorg-opnsense-frr-bgp-redistribution)            | stable |
| **Dynamic Routing**       | fyrastack.opnsense.frr_bgp_peer_group                             | [Docs](https://ansible-opnsense.oxl.app/modules/frr_bgp.html#oxlorg-opnsense-frr-bgp-peer-group)                | stable |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf_general                               | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf-general)                 | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf_prefix_list                           | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf-prefix-list)             | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf_route_map                             | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf-route-map)               | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf_interface                             | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf-interface)               | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf_network                               | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf-network)                 | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf_redistribution                        | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf-redistribution)          | stable |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf3_general                              | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf3-general)                | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf3_prefix_list                          | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf3-prefix-list)            | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf3_route_map                            | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf3-route-map)              | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf3_interface                            | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf3-interface)              | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf3_network                              | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf3-network)                | stable   |
| **Dynamic Routing**       | fyrastack.opnsense.frr_ospf3_redistribution                       | [Docs](https://ansible-opnsense.oxl.app/modules/frr_ospf.html#oxlorg-opnsense-frr-ospf3-redistribution)         | stable |
| **Dynamic Routing**       | fyrastack.opnsense.frr_rip                                        | [Docs](https://ansible-opnsense.oxl.app/modules/frr_rip.html)                                                   | stable   |
| **DNS**                   | fyrastack.opnsense.bind_general                                   | [Docs](https://ansible-opnsense.oxl.app/modules/bind.html#oxlorg-opnsense-bind-general)                         | stable   |
| **DNS**                   | fyrastack.opnsense.bind_blocklist                                 | [Docs](https://ansible-opnsense.oxl.app/modules/bind.html#oxlorg-opnsense-bind-blocklist)                       | stable   |
| **DNS**                   | fyrastack.opnsense.bind_acl                                       | [Docs](https://ansible-opnsense.oxl.app/modules/bind.html#oxlorg-opnsense-bind-acl)                             | stable   |
| **DNS**                   | fyrastack.opnsense.bind_domain                                    | [Docs](https://ansible-opnsense.oxl.app/modules/bind.html#oxlorg-opnsense-bind-domain)                          | stable   |
| **DNS**                   | fyrastack.opnsense.bind_record                                    | [Docs](https://ansible-opnsense.oxl.app/modules/bind.html#oxlorg-opnsense-bind-record)                          | stable   |
| **DNS**                   | fyrastack.opnsense.bind_record_multi                              | [Docs](https://ansible-opnsense.oxl.app/modules/bind.html#oxlorg-opnsense-bind-record-multi)                    | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_general                               | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id2)                                              | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_cache                                 | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id3)                                              | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_parent                                | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id4)                                              | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_traffic                               | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id5)                                              | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_forward                               | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id7)                                              | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_acl                                   | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id8)                                              | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_icap                                  | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id9)                                              | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_auth                                  | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id10)                                             | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_remote_acl                            | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id12)                                             | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_pac_proxy                             | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id14)                                             | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_pac_match                             | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id15)                                             | stable   |
| **Web Proxy**             | fyrastack.opnsense.webproxy_pac_rule                              | [Docs](https://ansible-opnsense.oxl.app/modules/webproxy.html#id18)                                             | stable   |
| **IDS/IPS**               | fyrastack.opnsense.ids_action                                     | [Docs](https://ansible-opnsense.oxl.app/modules/ids.html#id2)                                                   | stable   |
| **IDS/IPS**               | fyrastack.opnsense.ids_general                                    | [Docs](https://ansible-opnsense.oxl.app/modules/ids.html#id3)                                                   | stable   |
| **IDS/IPS**               | fyrastack.opnsense.ids_ruleset                                    | [Docs](https://ansible-opnsense.oxl.app/modules/ids.html#id4)                                                   | stable   |
| **IDS/IPS**               | fyrastack.opnsense.ids_rule                                       | [Docs](https://ansible-opnsense.oxl.app/modules/ids.html#id5)                                                   | stable   |
| **IDS/IPS**               | fyrastack.opnsense.ids_user_rule                                  | [Docs](https://ansible-opnsense.oxl.app/modules/ids.html#id6)                                                   | stable   |
| **IDS/IPS**               | fyrastack.opnsense.ids_policy                                     | [Docs](https://ansible-opnsense.oxl.app/modules/ids.html#id7)                                                   | stable   |
| **IDS/IPS**               | fyrastack.opnsense.ids_policy_rule                                | [Docs](https://ansible-opnsense.oxl.app/modules/ids.html#id8)                                                   | stable   |
| **OpenVPN**               | fyrastack.opnsense.openvpn_client                                 | [Docs](https://ansible-opnsense.oxl.app/modules/openvpn.html)                                                   | stable   |
| **OpenVPN**               | fyrastack.opnsense.openvpn_server                                 | [Docs](https://ansible-opnsense.oxl.app/modules/openvpn.html)                                                   | stable   |
| **OpenVPN**               | fyrastack.opnsense.openvpn_static_key                             | [Docs](https://ansible-opnsense.oxl.app/modules/openvpn.html)                                                   | stable   |
| **OpenVPN**               | fyrastack.opnsense.openvpn_status                                 | [Docs](https://ansible-opnsense.oxl.app/modules/openvpn.html)                                                   | stable   |
| **OpenVPN**               | fyrastack.opnsense.openvpn_client_override                        | [Docs](https://ansible-opnsense.oxl.app/modules/openvpn.html)                                                   | stable   |
| **Nginx**                 | fyrastack.opnsense.nginx_general                                  | [Docs](https://ansible-opnsense.oxl.app/modules/nginx.html#oxlorg-opnsense-nginx-general)                       | stable |
| **Nginx**                 | fyrastack.opnsense.nginx_upstream_server                          | [Docs](https://ansible-opnsense.oxl.app/modules/nginx.html#oxlorg-opnsense-nginx-upstream-server)               | stable |
| **DHCP Relay**            | fyrastack.opnsense.dhcrelay_relay                                 | [Docs](https://ansible-opnsense.oxl.app/modules/dhcrelay_relay.html)                                            | stable |
| **DHCP Relay**            | fyrastack.opnsense.dhcrelay_destination                           | [Docs](https://ansible-opnsense.oxl.app/modules/dhcrelay_destination.html)                                      | stable |
| **DHCP**                  | fyrastack.opnsense.dhcp_general                                   | [Docs](https://ansible-opnsense.oxl.app/modules/dhcp.html)                                                      | stable |
| **DHCP Subnet**           | fyrastack.opnsense.dhcp_subnet                                    | [Docs](https://ansible-opnsense.oxl.app/modules/dhcp.html)                                                      | stable |
| **DHCP Reservation**      | fyrastack.opnsense.dhcp_reservation                               | [Docs](https://ansible-opnsense.oxl.app/modules/dhcp.html)                                                      | stable |
| **DHCP Controlagent**     | fyrastack.opnsense.dhcp_controlagent                              | [Docs](https://ansible-opnsense.oxl.app/modules/dhcp.html)                                                      | stable |
| **ACME (Certificates)**   | fyrastack.opnsense.acme_account                                   | [Docs](https://ansible-opnsense.oxl.app/modules/acmeclient.html)                                                | stable |
| **ACME (Certificates)**   | fyrastack.opnsense.acme_action                                    | [Docs](https://ansible-opnsense.oxl.app/modules/acmeclient.html)                                                | stable |
| **ACME (Certificates)**   | fyrastack.opnsense.acme_general                                   | [Docs](https://ansible-opnsense.oxl.app/modules/acmeclient.html)                                                | stable |
| **ACME (Certificates)**   | fyrastack.opnsense.acme_validation                                | [Docs](https://ansible-opnsense.oxl.app/modules/acmeclient.html)                                                | stable |
| **ACME (Certificates)**   | fyrastack.opnsense.acme_certificate                               | [Docs](https://ansible-opnsense.oxl.app/modules/acmeclient.html)                                                | stable |
| **Postfix**               | fyrastack.opnsense.postfix_general                                | [Docs](https://ansible-opnsense.oxl.app/modules/postfix.html)                                                   | stable |
| **Postfix**               | fyrastack.opnsense.postfix_domain                                 | [Docs](https://ansible-opnsense.oxl.app/modules/postfix.html)                                                   | stable |
| **Postfix**               | fyrastack.opnsense.postfix_recipient                              | [Docs](https://ansible-opnsense.oxl.app/modules/postfix.html)                                                   | stable |
| **Postfix**               | fyrastack.opnsense.postfix_recipientbcc                           | [Docs](https://ansible-opnsense.oxl.app/modules/postfix.html)                                                   | stable |
| **Postfix**               | fyrastack.opnsense.postfix_sender                                 | [Docs](https://ansible-opnsense.oxl.app/modules/postfix.html)                                                   | stable |
| **Postfix**               | fyrastack.opnsense.postfix_senderbcc                              | [Docs](https://ansible-opnsense.oxl.app/modules/postfix.html)                                                   | stable |
| **Postfix**               | fyrastack.opnsense.postfix_sendercanonical                        | [Docs](https://ansible-opnsense.oxl.app/modules/postfix.html)                                                   | stable |
| **Postfix**               | fyrastack.opnsense.postfix_headercheck                            | [Docs](https://ansible-opnsense.oxl.app/modules/postfix.html)                                                   | stable |
| **Postfix**               | fyrastack.opnsense.postfix_address                                | [Docs](https://ansible-opnsense.oxl.app/modules/postfix.html)                                                   | stable |
| **Snapshot**              | fyrastack.opnsense.snapshot                                       | [Docs](https://ansible-opnsense.oxl.app/modules/snapshot.html)                                                  | stable |
| **High Availability**     | fyrastack.opnsense.hasync_general                                 | [Docs](https://ansible-opnsense.oxl.app/modules/hasync.html)                                                    | stable |
| **High Availability**     | fyrastack.opnsense.hasync_service                                 | [Docs](https://ansible-opnsense.oxl.app/modules/hasync.html)                                                    | stable |
| **User Management**       | fyrastack.opnsense.user                                           | [Docs](https://ansible-opnsense.oxl.app/modules/access.html)                                                    | unstable |
| **User Management**       | fyrastack.opnsense.group                                          | [Docs](https://ansible-opnsense.oxl.app/modules/access.html)                                                    | unstable |
| **User Management**       | fyrastack.opnsense.privilege                                      | [Docs](https://ansible-opnsense.oxl.app/modules/access.html)                                                    | unstable |
| **Neighbor**              | fyrastack.opnsense.neighbor                                       | [Docs](https://ansible-opnsense.oxl.app/modules/neighbor.html)                                                  | unstable |
| **Dnsmasq**               | fyrastack.opnsense.dnsmasq_general                                | [Docs](https://ansible-opnsense.oxl.app/modules/dnsmasq.html)                                                   | unstable |
| **Dnsmasq**               | fyrastack.opnsense.dnsmasq_domain                                 | [Docs](https://ansible-opnsense.oxl.app/modules/dnsmasq.html)                                                   | unstable |
| **Dnsmasq**               | fyrastack.opnsense.dnsmasq_host                                   | [Docs](https://ansible-opnsense.oxl.app/modules/dnsmasq.html)                                                   | unstable |
| **Dnsmasq**               | fyrastack.opnsense.dnsmasq_range                                  | [Docs](https://ansible-opnsense.oxl.app/modules/dnsmasq.html)                                                   | unstable |
| **Dnsmasq**               | fyrastack.opnsense.dnsmasq_option                                 | [Docs](https://ansible-opnsense.oxl.app/modules/dnsmasq.html)                                                   | unstable |
| **Dnsmasq**               | fyrastack.opnsense.dnsmasq_boot                                   | [Docs](https://ansible-opnsense.oxl.app/modules/dnsmasq.html)                                                   | unstable |
| **Dnsmasq**               | fyrastack.opnsense.dnsmasq_tag                                    | [Docs](https://ansible-opnsense.oxl.app/modules/dnsmasq.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_general_cache                          | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_general_defaults                       | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_general_logging                        | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_general_peers                          | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_general_settings                       | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_general_stats                          | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_general_tuning                         | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_cpu                                    | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_user                                   | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_group                                  | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_maintenance                            | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_acl                                    | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_lua                                    | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_action                                 | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_errorfile                              | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |
| **HAProxy**               | fyrastack.opnsense.haproxy_fcgi                                   | [Docs](https://ansible-opnsense.oxl.app/modules/haproxy.html)                                                   | unstable |

### Roadmap

See: [Feature Requests](https://github.com/O-X-L/ansible-opnsense/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement)
