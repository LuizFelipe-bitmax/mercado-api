from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def obter_token():

    response = client.post(
        "/login",
        data={
            "username": "luizfelipe",
            "password": "123456"
        }
    )

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }