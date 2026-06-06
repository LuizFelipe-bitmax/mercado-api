from fastapi import (
    Request,
    status
)

from fastapi.responses import (
    JSONResponse
)

from fastapi.exceptions import (
    RequestValidationError
)

from starlette.exceptions import (
    HTTPException as StarletteHTTPException
)


async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException
):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "erro": exc.detail
        }
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "erro": "Dados inválidos",
            "detalhes": exc.errors()
        }
    )


async def internal_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "erro": "Erro interno do servidor"
        }
    )