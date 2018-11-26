import pytest
from packages.http_client.http_client import HttpClient


@pytest.fixture(scope="function")
def http_client():
    return HttpClient()
