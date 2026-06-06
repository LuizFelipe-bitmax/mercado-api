from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_login():

    response = client.post(
        "/login",
        data={
            "username": "luizfelipe",
            "password": "123456"
        }
    )

    assert response.status_code == 200

    dados = response.json()

    assert "access_token" in dados

    assert dados["token_type"] == "bearer"