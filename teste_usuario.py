from database.connection import SessionLocal
from models.usuario import Usuario


db = SessionLocal()

novo_usuario = Usuario(
    username="luiz",
    password="123456"
)

db.add(novo_usuario)

db.commit()

print("Usuário criado!")

db.close()