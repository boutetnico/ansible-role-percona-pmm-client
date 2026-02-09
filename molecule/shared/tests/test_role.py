import pytest
import json


@pytest.mark.parametrize(
    "name",
    [
        ("percona-release"),
        ("pmm-client"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_pmm_admin_binary_exists(host):
    """Test that pmm-admin binary exists and is executable."""
    f = host.file("/usr/sbin/pmm-admin")
    assert f.exists
    assert f.is_file
    assert f.mode & 0o111  # Check executable bit


def test_pmm_admin_version(host):
    """Test that pmm-admin can be executed and returns version."""
    cmd = host.run("pmm-admin --version")
    assert cmd.rc == 0
    assert "pmm-admin" in cmd.stdout.lower()


def test_pmm_admin_status(host):
    """Test that pmm-admin status works."""
    cmd = host.run("pmm-admin status")
    assert cmd.rc == 0


@pytest.mark.parametrize(
    "service_name,service_type",
    [
        ("service-mongodb", "mongodb"),
        ("service-mysql", "mysql"),
    ],
)
def test_pmm_services_registered(host, service_name, service_type):
    """Test that PMM services are registered."""
    json_data = host.check_output("pmm-admin list --json")
    pmm_list = json.loads(json_data)

    service_found = False
    for service in pmm_list["service"]:
        if service["service_name"] == service_name:
            service_found = True
            # Verify the service type matches
            assert service_type in service["service_type"].lower()
            break

    assert service_found, f"Service {service_name} not found in PMM services"


def test_pmm_config_file_exists(host):
    """Test that PMM agent config file exists."""
    f = host.file("/usr/local/percona/pmm-agent.yml")
    assert f.exists
    assert f.is_file
