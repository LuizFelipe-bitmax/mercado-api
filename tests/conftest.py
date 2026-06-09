from fastapi.testclient import TestClient

from main import app
from database.base import Base
from database.connection import engine

from models.usuario import Usuario
from models.produtos import Produto

Base.metadata.create_all(bind=engine)

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