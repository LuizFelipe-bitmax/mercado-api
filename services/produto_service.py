from sqlalchemy.orm import Session

from models.produtos import Produto


def listar_produtos(
    db: Session,
    skip=0,
    limit=10,
    ordenar=None
):

    query = db.query(
        Produto
    )

    if ordenar == "nome":

        query = query.order_by(
            Produto.nome
        )

    elif ordenar == "preco":

        query = query.order_by(
            Produto.preco
        )

    elif ordenar == "estoque":

        query = query.order_by(
            Produto.estoque
        )

    elif ordenar == "categoria":

        query = query.order_by(
            Produto.categoria
        )

    return query.offset(
        skip
    ).limit(
        limit
    ).all()


def buscar_produto(
    produto_id,
    db: Session
):

    return db.query(
        Produto
    ).filter(
        Produto.id == produto_id
    ).first()


def criar_produto(
    produto,
    db: Session
):

    novo_produto = Produto(
        nome=produto.nome,
        preco=produto.preco,
        estoque=produto.estoque,
        categoria=produto.categoria
    )

    db.add(
        novo_produto
    )

    db.commit()

    db.refresh(
        novo_produto
    )

    return novo_produto


def atualizar_produto(
    produto_id,
    produto,
    db: Session
):

    produto_db = buscar_produto(
        produto_id,
        db
    )

    if not produto_db:
        return None

    produto_db.nome = produto.nome
    produto_db.preco = produto.preco
    produto_db.estoque = produto.estoque
    produto_db.categoria = produto.categoria

    db.commit()

    db.refresh(
        produto_db
    )

    return produto_db


def deletar_produto(
    produto_id,
    db: Session
):

    produto_db = buscar_produto(
        produto_id,
        db
    )

    if not produto_db:
        return False

    db.delete(
        produto_db
    )

    db.commit()

    return True


def filtrar_produtos(
    db: Session,
    categoria=None,
    nome=None,
    limit=10,
    offset=0,
    ordenar=None
):

    query = db.query(
        Produto
    )

    if categoria:

        query = query.filter(
            Produto.categoria.ilike(
                f"%{categoria}%"
            )
        )

    if nome:

        query = query.filter(
            Produto.nome.ilike(
                f"%{nome}%"
            )
        )

    if ordenar == "nome":

        query = query.order_by(
            Produto.nome
        )

    elif ordenar == "preco":

        query = query.order_by(
            Produto.preco
        )

    elif ordenar == "estoque":

        query = query.order_by(
            Produto.estoque
        )

    elif ordenar == "categoria":

        query = query.order_by(
            Produto.categoria
        )

    return query.offset(
        offset
    ).limit(
        limit
    ).all()