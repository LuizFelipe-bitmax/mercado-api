from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query
)

from sqlalchemy.orm import Session

from schemas.produto import (
    ProdutoCreate,
    ProdutoResponse
)

from security.deps import (
    get_usuario_logado
)

from database.session import (
    get_db
)

from services.produto_service import (
    buscar_produto,
    criar_produto,
    atualizar_produto,
    deletar_produto,
    filtrar_produtos
)

router_produtos = APIRouter()


@router_produtos.get(
    "/produtos",
    response_model=list[ProdutoResponse]
)
def rota_listar_produtos(
    categoria: str | None = Query(
        default=None
    ),
    nome: str | None = Query(
        default=None
    ),
    limit: int = Query(
        default=10,
        ge=1,
        le=100
    ),
    offset: int = Query(
        default=0,
        ge=0
    ),
    ordenar: str | None = Query(
        default=None
    ),
    db: Session = Depends(get_db),
    usuario: str = Depends(
        get_usuario_logado
    )
):

    return filtrar_produtos(
        db=db,
        categoria=categoria,
        nome=nome,
        limit=limit,
        offset=offset,
        ordenar=ordenar
    )


@router_produtos.get(
    "/produtos/{produto_id}",
    response_model=ProdutoResponse
)
def rota_buscar_produto(
    produto_id: int,
    db: Session = Depends(get_db),
    usuario: str = Depends(
        get_usuario_logado
    )
):

    produto = buscar_produto(
        produto_id,
        db
    )

    if not produto:

        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return produto


@router_produtos.post(
    "/produtos",
    response_model=ProdutoResponse
)
def rota_criar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db),
    usuario: str = Depends(
        get_usuario_logado
    )
):

    return criar_produto(
        produto,
        db
    )


@router_produtos.put(
    "/produtos/{produto_id}",
    response_model=ProdutoResponse
)
def rota_atualizar_produto(
    produto_id: int,
    produto: ProdutoCreate,
    db: Session = Depends(get_db),
    usuario: str = Depends(
        get_usuario_logado
    )
):

    produto_atualizado = atualizar_produto(
        produto_id,
        produto,
        db
    )

    if not produto_atualizado:

        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return produto_atualizado


@router_produtos.delete(
    "/produtos/{produto_id}"
)
def rota_deletar_produto(
    produto_id: int,
    db: Session = Depends(get_db),
    usuario: str = Depends(
        get_usuario_logado
    )
):

    sucesso = deletar_produto(
        produto_id,
        db
    )

    if not sucesso:

        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return {
        "mensagem": "Produto removido com sucesso"
    }