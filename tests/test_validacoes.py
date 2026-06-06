from fastapi.testclient import TestClient

from main import app

from tests.conftest import obter_token

client = TestClient(app)


def test_produto_preco_negativo():

    headers = obter_token()

    response = client.post(
        "/produtos",
        headers=headers,
        json={
            "nome": "Sabão",
            "preco": -10,
            "estoque": 5,
            "categoria": "Limpeza"
        }
    )

    assert response.status_code == 422


def test_produto_estoque_negativo():

    headers = obter_token()

    response = client.post(
        "/produtos",
        headers=headers,
        json={
            "nome": "Sabão",
            "preco": 10,
            "estoque": -1,
            "categoria": "Limpeza"
        }
    )

    assert response.status_code == 422


def test_produto_nome_vazio():

    headers = obter_token()

    response = client.post(
        "/produtos",
        headers=headers,
        json={
            "nome": "",
            "preco": 10,
            "estoque": 5,
            "categoria": "Limpeza"
        }
    )

    assert response.status_code == 422