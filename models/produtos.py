from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from database.base import Base


class Produto(Base):

    __tablename__ = "produtos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nome = Column(
        String,
        nullable=False
    )

    preco = Column(
        Float,
        nullable=False
    )

    estoque = Column(
        Integer,
        nullable=False
    )

    categoria = Column(
        String,
        nullable=False
    )