from fastapi import (
    Depends,
    HTTPException
)

from fastapi.security import (
    OAuth2PasswordBearer
)

from jose import (
    jwt,
    JWTError
)

SECRET_KEY = "123456"

ALGORITHM = "HS256"


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


def get_usuario_logado(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Token inválido"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token inválido ou expirado"
        )