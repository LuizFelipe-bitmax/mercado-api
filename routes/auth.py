from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from fastapi.security import (
    OAuth2PasswordRequestForm
)

from sqlalchemy.orm import Session

from schemas.usuario import UsuarioCreate

from services.usuario_service import (
    criar_usuario,
    autenticar_usuario
)

from security.jwt_handler import (
    criar_token
)

from database.session import (
    get_db
)

router_auth = APIRouter(
    tags=["Autenticação"]
)


@router_auth.post(
    "/cadastro",
    summary="Cadastrar usuário",
    description="""
Cria um novo usuário no sistema.

Regras:
- Username deve ser único.
- Senha será armazenada criptografada.
""",
    responses={
        200: {
            "description": "Usuário criado com sucesso"
        },
        409: {
            "description": "Usuário já existe"
        }
    }
)
def rota_cadastro(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):

    novo_usuario = criar_usuario(
        usuario,
        db
    )

    if novo_usuario is None:

        raise HTTPException(
            status_code=409,
            detail="Usuário já existe"
        )

    return {
        "mensagem": "Usuário criado",
        "dados": {
            "id": novo_usuario.id,
            "username": novo_usuario.username
        }
    }


@router_auth.post(
    "/login",
    summary="Realizar login",
    description="""
Autentica um usuário e retorna um token JWT.

Utilize o token retornado para acessar
rotas protegidas da API.
""",
    responses={
        200: {
            "description": "Login realizado com sucesso"
        },
        401: {
            "description": "Credenciais inválidas"
        }
    }
)
def rota_login(
    formulario: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    usuario = autenticar_usuario(
        formulario.username,
        formulario.password,
        db
    )

    if not usuario:

        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas"
        )

    token = criar_token({
        "sub": usuario.username
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }