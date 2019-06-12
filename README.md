# Ansible playbook for RHEL OS hardening

## Usage instructions

1. Customize vars/os-vars.yml file carefully before running the playbook.
2. Run the playbook
```
ansible-playbook os-harden.yml
```

## Requirements

- Run on RedHat Enterprise Linux only using rsyslog as the message logging utility.
- Python 2.7 or later.

## Dependencies

None

## License
GPLv3

## Author Information
Marcin Bazyluk, bazyluk@gmail.com
No support is given.

