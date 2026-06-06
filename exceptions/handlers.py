from fastapi import (
    Request,
    HTTPException
)

from fastapi.responses import (
    JSONResponse
)

from fastapi.exceptions import (
    RequestValidationError
)


async def http_exception_handler(
    request: Request,
    exc: HTTPException
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
        status_code=422,
        content={
            "erro": "Dados inválidos",
            "detalhes": exc.errors()
        }
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "erro": "Erro interno do servidor"
        }
    )