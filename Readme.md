[![tests](https://github.com/boutetnico/ansible-role-pmm-client/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-pmm-client/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.pmm_client-blue.svg)](https://galaxy.ansible.com/boutetnico/pmm_client)

ansible-role-pmm-client
=======================

This role installs [PMM client](https://www.percona.com/doc/percona-monitoring-and-management/2.x/manage/index-using-pmm-client.html).

It is part of a family of Ansible roles allowing to setup and configure PMM:

- [ansible-role-pmm-server](https://github.com/boutetnico/ansible-role-pmm-server)
- [ansible-role-pmm-client](https://github.com/boutetnico/ansible-role-pmm-client)

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                       | Required | Default                             | Choices | Comments                                       |
|--------------------------------|----------|-------------------------------------|---------|------------------------------------------------|
| pmm_client_server_url          | true     | `https://admin:admin@127.0.0.1:443` | string  |                                                |
| pmm_client_server_insecure_tls | true     | `false`                             | bool    |                                                |
| pmm_client_package_state       | true     | `present`                           | string  | Use `latest` to upgrade PMM client.            |
| pmm_client_services            | true     | `[]`                                | list    | Services to configure. See `defaults/main.yml`.|

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-pmm-client
          pmm_client_server_insecure_tls: true
          pmm_client_services:
            - type: mysql
              name: "service-mysql"
              flags: "--username=root --password=root"
            - type: mongodb
              name: "service-mongodb"
              flags: "--port=27017"

Testing
-------

## Debian

    molecule --base-config molecule/shared/base.yml test --scenario-name debian-11
    molecule --base-config molecule/shared/base.yml test --scenario-name debian-12

## Ubuntu

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-2204

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
