from sqlalchemy.orm import Session

from models.usuario import Usuario

from security.jwt_handler import (
    gerar_hash,
    verificar_senha
)


def criar_usuario(
    usuario,
    db: Session
):

    usuario_existente = db.query(
        Usuario
    ).filter(
        Usuario.username == usuario.username
    ).first()

    if usuario_existente:
        return None

    senha_hash = gerar_hash(
        usuario.password
    )

    novo_usuario = Usuario(
        username=usuario.username,
        password=senha_hash
    )

    db.add(
        novo_usuario
    )

    db.commit()

    db.refresh(
        novo_usuario
    )

    return novo_usuario


def autenticar_usuario(
    username,
    password,
    db: Session
):

    usuario = db.query(
        Usuario
    ).filter(
        Usuario.username == username
    ).first()

    if not usuario:
        return None

    if not verificar_senha(
        password,
        usuario.password
    ):
        return None

    return usuario