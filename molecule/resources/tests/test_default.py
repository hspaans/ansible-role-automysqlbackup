"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize("pkg", ["automysqlbackup"])
def test_pkg_installed(host, pkg):
    """Test if package installed."""
    package = host.package(pkg)

    assert package.is_installed
