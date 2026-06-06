from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)


def test_cadastro():

    username_unico = f"usuario_{uuid.uuid4().hex[:8]}"

    response = client.post(
        "/cadastro",
        json={
            "username": username_unico,
            "password": "123456"
        }
    )

    assert response.status_code == 200

    dados = response.json()

    assert dados["dados"]["username"] == username_unico