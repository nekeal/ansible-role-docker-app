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
