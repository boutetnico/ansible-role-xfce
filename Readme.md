[![tests](https://github.com/boutetnico/ansible-role-xfce/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-xfce/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.xfce-blue.svg)](https://galaxy.ansible.com/boutetnico/xfce)

ansible-role-xfce
=================

This role installs [Xfce Desktop Environment](https://www.xfce.org/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                | Required | Default               | Choices   | Comments                                       |
|-------------------------|----------|-----------------------|-----------|------------------------------------------------|
| xfce_dependencies       | yes      | `[lightdm]`           | list      |                                                |
| xfce_packages           | yes      | `[xfce4]`             | list      |                                                |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-xfce

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
