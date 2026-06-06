from fastapi.testclient import TestClient

from main import app

from tests.conftest import obter_token

client = TestClient(app)


def test_inicio():

    response = client.get("/")

    assert response.status_code == 200


def test_produto_inexistente():

    headers = obter_token()

    response = client.get(
        "/produtos/9999",
        headers=headers
    )

    assert response.status_code == 404