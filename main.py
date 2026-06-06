from fastapi import FastAPI

from fastapi.exceptions import (
    RequestValidationError
)

from starlette.exceptions import (
    HTTPException as StarletteHTTPException
)

from routes.produtos import router_produtos
from routes.auth import router_auth

from handlers.exception_handlers import (
    http_exception_handler,
    validation_exception_handler,
    internal_exception_handler
)

app = FastAPI(
    title="Mercado API",
    description="""
API de gerenciamento de produtos e usuários.

Funcionalidades:

- Cadastro de usuários
- Login com JWT
- CRUD de produtos
- Filtros por categoria e nome
- Paginação
- Ordenação
- Validações com Pydantic
""",
    version="1.0.0",
    contact={
        "name": "Luiz Felipe",
        "email": "luizfelipe@email.com"
    }
)

app.add_exception_handler(
    StarletteHTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    internal_exception_handler
)

app.include_router(router_produtos)
app.include_router(router_auth)


@app.get(
    "/",
    tags=["Sistema"],
    summary="Verificar status da API",
    description="Retorna uma mensagem indicando que a API está funcionando."
)
def inicio():

    return {
        "mensagem": "Mercado API funcionando"
    }