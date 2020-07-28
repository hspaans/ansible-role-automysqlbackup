Role Name
=========


Installs [autmysqlbackup](https://sourceforge.net/projects/automysqlbackup/).

Requirements
------------

None.

Role Variables
--------------

Default variables are set in `defaults/main.yml` to match the WP-CLI and role version.

Dependencies
------------

No dependency on other Ansible Galaxy roles.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: hspaans.automysqlbackup, become: true }

License
-------

MIT

Author Information
------------------

This role was created in 2020 by [Hans Spaans](https://github.com/hspaans).