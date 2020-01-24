gabops.docker
=============
[![Build Status](https://travis-ci.org/gabops/ansible-role-docker.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-docker)

Installs and Configures Docker Community Edition.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| docker_engine_version | latest | Defines the version of Docker Engine to be installed.  |
| docker_cli_version | latest | Defines the version of Docker CLI to be installed. |
| docker_release_channel | stable | Defines the release channel to install Docker from. Possible values are `stable`, `test` and `nigthly`. |
| docker_service_enabled | true | Controls if the Docker service should be enabled or not in order to be started when the system boots. |
| docker_service_state | started | Defines the status of the Docker service. Typical values here are `started` or `stopped` |
| docker_daemon_config | "" | Defines the settings to be applied on `/etc/docker/daemon.json` in order to configure the Docker service. |
| docker_group_members | [] | Defines the `users` and/or `groups` to be added to the `docker` group. Note that this role does **not create** users nor groups, it just **appends** existing users and groups to the docker group. |

### Notes:
- On Debian family distributions could be required to specifiy the [epoch](https://manpages.debian.org/stretch/dpkg-dev/deb-version.5.en.html) number when declaring the version on `docker_engine_version` and/or `docker_cli_version`. For example:

```yaml
    docker_engine_version: "5:18.09"
    docker_cli_version: "5:19.03"
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: docker
  vars:
    docker_engine_version: 18.09
    docker_cli_version: 19.03.2
    docker_daemon_config:
      data-root: "/mnt/docker"
      log-level: "debug"
      storage-driver: "vfs"
      log-driver: "json-file"
      log-opts:
        max-size: "10m"
        max-file: "3"
    docker_group_members:
      - devops
      - john.doe

  roles:
    - role: gabops.docker

```

License
-------

[MIT](./LICENSE)

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops/))
