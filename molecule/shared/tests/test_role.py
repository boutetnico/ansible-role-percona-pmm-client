import pytest

import os

import json

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "name",
    [
        ("percona-release"),
        ("pmm2-client"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "service_name",
    [
        ("service-mongodb"),
        ("service-mysql"),
    ],
)
def test_crontab_jobs_exist(host, service_name):
    json_data = host.check_output("pmm-admin list --json")
    pmm_list = json.loads(json_data)
    for service in pmm_list["service"]:
        if service["service_name"] == service_name:
            assert True
            break
    else:
        assert False
