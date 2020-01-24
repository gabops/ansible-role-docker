import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_service(host):
    s = host.service('docker')

    assert s.is_enabled
    assert s.is_running


def test_docker_run(host):
    c = host.run('docker run hello-world')

    assert 'Hello from Docker!' in c.stdout
