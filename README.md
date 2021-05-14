# Role Name

Installs [automysqlbackup](https://sourceforge.net/projects/automysqlbackup/).

## Requirements

None.

## Role Variables

Default variables are set in `defaults/main.yml` to match the WP-CLI and role version.

## Dependencies

No dependency on other Ansible Galaxy roles.

## Platforms

The role is tested agains [LTS](https://en.wikipedia.org/wiki/Long-term_support) distribution versions with official support and fall within N and N-1.

## Example Playbook

```yaml
---
- hosts: servers
  roles:
    - role: hspaans.automysqlbackup
      become: true
```

## License

MIT

## Author Information

This role was created in 2020 by [Hans Spaans](https://github.com/hspaans).
