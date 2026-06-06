from jose import jwt

from datetime import (
    datetime,
    timedelta,
    UTC
)

from passlib.context import CryptContext

from config import (
    SECRET_KEY,
    ALGORITHM,
    TEMPO_EXPIRACAO
)


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def gerar_hash(
    senha
):

    return pwd_context.hash(
        senha
    )


def verificar_senha(
    senha_normal,
    senha_hash
):

    return pwd_context.verify(
        senha_normal,
        senha_hash
    )


def criar_token(
    dados: dict
):

    dados_copia = dados.copy()

    expiracao = datetime.now(
        UTC
    ) + timedelta(
        minutes=TEMPO_EXPIRACAO
    )

    dados_copia.update(
        {
            "exp": expiracao
        }
    )

    token = jwt.encode(
        dados_copia,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token