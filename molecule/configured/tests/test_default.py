import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker(host):
    c = host.run('docker info').rc

    assert c == 0


def test_docker_service(host):
    s = host.service('docker')

    assert s.is_enabled
    assert s.is_running


def test_docker_version(host):
    docker = host.package("docker-ce")

    assert docker.is_installed
    assert "18.09" in docker.version


def test_docker_cli_version(host):
    docker_cli = host.package("docker-ce-cli")

    assert docker_cli.is_installed
    assert "19.03" in docker_cli.version


def test_docker_run(host):
    c = host.run('docker run hello-world')

    assert 'Hello from Docker!' in c.stdout
