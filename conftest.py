"""
Contain fixture.
"""

import pytest
from functional.configuration import Configuration


@pytest.fixture(scope="session")
def conf(request):
    """Create functional."""
    fixture = Configuration()
    fixture.session.login(email="taqc296@gmail.com", password="root")

    def close():
        """Close functional."""
        fixture.session.logout()
        fixture.exit_fixture()

    request.addfinalizer(close)
    return fixture
