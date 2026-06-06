from database.connection import engine
from database.base import Base

from models.usuario import Usuario
from models.produtos import Produto

print("Criando tabelas...")

Base.metadata.create_all(
    bind=engine
)

print("Tabelas criadas!")