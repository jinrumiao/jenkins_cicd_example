from fastapi.testclient import TestClient
from api_example import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a fastapi example."}


def test_hello():
    response = client.get("/v1/hello?name=Jin")
    assert response.status_code == 200
    assert response.json() == {"data": "Hello Jin."}
