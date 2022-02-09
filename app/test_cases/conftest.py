from run import create_app

import pytest


@pytest.fixture
def client():
    flask_app = create_app()
    with flask_app.app.test_client() as client:
        yield client

