from fastapi.testclient import TestClient

from main import app

from tests.conftest import obter_token

client = TestClient(app)


def test_atualizar_produto():

    headers = obter_token()

    response_criar = client.post(
        "/produtos",
        headers=headers,
        json={
            "nome": "Mouse Gamer",
            "preco": 150.0,
            "estoque": 10,
            "categoria": "Periféricos"
        }
    )

    produto_id = response_criar.json()["id"]

    response = client.put(
        f"/produtos/{produto_id}",
        headers=headers,
        json={
            "nome": "Mouse Gamer Pro",
            "preco": 200.0,
            "estoque": 15,
            "categoria": "Periféricos"
        }
    )

    assert response.status_code == 200

    dados = response.json()

    assert dados["nome"] == "Mouse Gamer Pro"


def test_deletar_produto():

    headers = obter_token()

    response_criar = client.post(
        "/produtos",
        headers=headers,
        json={
            "nome": "Teclado",
            "preco": 120.0,
            "estoque": 5,
            "categoria": "Periféricos"
        }
    )

    produto_id = response_criar.json()["id"]

    response = client.delete(
        f"/produtos/{produto_id}",
        headers=headers
    )

    assert response.status_code == 200

    assert (
        response.json()["mensagem"]
        ==
        "Produto removido com sucesso"
    )


def test_produto_nao_encontrado():

    headers = obter_token()

    response = client.get(
        "/produtos/999999",
        headers=headers
    )

    assert response.status_code == 404