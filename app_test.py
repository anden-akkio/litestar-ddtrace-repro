import pytest
import app
from litestar.testing import TestClient

@pytest.fixture
def client() -> TestClient:
    return TestClient(app=app.app)

def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert 200 <= response.status_code < 300