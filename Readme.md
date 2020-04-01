ansible-role-pmm-client
=======================

This role installs PMM client.

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)

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

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1604
    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1804

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
