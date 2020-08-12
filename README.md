docker-app
=========

Role which installs and deploys containerized apllications

Requirements
------------

To develop this role you should install requirements via `pip install -r requirements.txt`

Role Variables
--------------
    docker_apt_key_url: https://download.docker.com/linux/{{ ansible_distribution | lower }}/gpg
    docker_apt_repository: "deb [arch=amd64] https://download.docker.com/linux/{{ ansible_distribution | lower }} {{ ansible_distribution_release }} stable"
    docker_edition: ce
    docker_apt_package_name: "docker-{{ docker_edition }}"

This variables control where should be docker installed from. You can overwrite `docker_apt_repository` for example to use different architecture than `amd64`.

    docker_service_name: docker

Defines name of docker service. Propably you will never change this.

    docker_host_default: unix://var/run/docker.sock
    docker_tls_hostname_default: localhost
    docker_api_verison_default: auto
    docker_timeout_default: 60

Defines common vars used by `docker_image` and `docker_container` modules. You can set almost all default variables used by docker images and containers for example you don't want to specify `state` of docker container for each container, so you can set `docker_state_default` variable which will be used by each item in `docker_containers` list.

    docker_images: []

List of dicts containing configuration in same format as requires `docker_image` module. Each parameter which is provided in module is available. You can also set global default value for each image.

    docker_containers: []

List of dicts containing configuration in same format as requires `docker_container` module. Each parameter which is provided in module is available. You can also set globally available default.

    docker_app_git_repositories: []

List of repositories to clone. You can use each argument provided by git module. You can also set default for every repo of a list with the folllowing convention:
`git_<argument_name>_default`, where `argument_name` is any argument in the git module.

**There is one exception: `update` argument. Due to conflict with builtin method `update` of dict it is renamed to `update_repo`!**

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: docker-app

License
-------

MIT

Author Information
------------------

nekeal
