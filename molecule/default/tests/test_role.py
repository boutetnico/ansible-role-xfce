import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("lightdm"),
        ("dbus-x11"),
    ],
)
def test_dependencies_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "name",
    [
        ("xfce4"),
        ("xfce4-terminal"),
    ],
)
def test_xfce_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_lightdm_service_enabled(host):
    service = host.service("lightdm")
    assert service.is_enabled


def test_xfce4_session_exists(host):
    # Check if xfce4-session binary exists
    cmd = host.run("which xfce4-session")
    assert cmd.rc == 0


def test_dbus_daemon_available(host):
    # Verify dbus-daemon is available (required for xfce)
    cmd = host.run("which dbus-daemon")
    assert cmd.rc == 0
