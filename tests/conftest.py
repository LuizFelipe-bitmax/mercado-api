from fastapi.testclient import TestClient

from main import app
from database.base import Base
from database.connection import engine, SessionLocal

from models.usuario import Usuario
from models.produtos import Produto

from security.jwt_handler import gerar_hash

Base.metadata.create_all(bind=engine)

db = SessionLocal()

usuario = db.query(Usuario).filter(
    Usuario.username == "luizfelipe"
).first()

if not usuario:

    usuario = Usuario(
        username="luizfelipe",
        password=gerar_hash("123456")
    )

    db.add(usuario)
    db.commit()

db.close()

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