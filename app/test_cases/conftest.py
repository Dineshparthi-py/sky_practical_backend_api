import pytest


@pytest.fixture
def market_url():
    """
    market summaries api base url
    """
    return "http://127.0.0.1:5000/api/v1"
