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

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

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

    molecule --base-config molecule/shared/base.yml test --scenario-name debian-9
    molecule --base-config molecule/shared/base.yml test --scenario-name debian-10

## Ubuntu

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1804
    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-2004

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
