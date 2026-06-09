# Mercado API

API REST desenvolvida com FastAPI para gerenciamento de produtos e usuários, utilizando autenticação JWT, SQLAlchemy, testes automatizados com Pytest e integração contínua com GitHub Actions.

## Funcionalidades

### Autenticação

* Cadastro de usuários
* Login com JWT
* Rotas protegidas por autenticação

### Produtos

* Criar produto
* Listar produtos
* Buscar produto por ID
* Atualizar produto
* Deletar produto

### Recursos Extras

* Filtros por categoria
* Busca por nome
* Paginação
* Ordenação de resultados
* Validações com Pydantic
* Tratamento global de exceções

---

## Tecnologias Utilizadas

### Backend

* Python 3.12
* FastAPI
* SQLAlchemy
* SQLite

### Segurança

* JWT (JSON Web Token)
* Passlib (Hash de Senhas)

### Testes

* Pytest
* FastAPI TestClient

### DevOps

* Git
* GitHub
* GitHub Actions (CI/CD)

---

## Estrutura do Projeto

mercado-api/

├── database/

│ ├── base.py

│ ├── connection.py

│ ├── create_tables.py

│ └── session.py

│

├── handlers/

│ └── exception_handlers.py

│

├── models/

│ ├── produtos.py

│ └── usuario.py

│

├── routes/

│ ├── auth.py

│ └── produtos.py

│

├── schemas/

│ ├── produto.py

│ └── usuario.py

│

├── security/

│ ├── deps.py

│ └── jwt_handler.py

│

├── services/

│ ├── produto_service.py

│ └── usuario_service.py

│

├── tests/

│ ├── conftest.py

│ ├── test_auth.py

│ ├── test_crud_produtos.py

│ ├── test_login.py

│ ├── test_main.py

│ ├── test_produtos.py

│ └── test_validacoes.py

│

├── config.py

├── main.py

├── requirements.txt

└── README.md

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/LuizFelipe-bitmax/mercado-api.git
cd mercado-api
```

Crie e ative o ambiente virtual:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
TEMPO_EXPIRACAO=30
```

---

## Criar Tabelas

```bash
python database/create_tables.py
```

---

## Executar a Aplicação

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

Documentação Swagger:

```text
http://127.0.0.1:8000/docs
```

Documentação ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Executar os Testes

```bash
pytest
```

---

## Integração Contínua

O projeto utiliza GitHub Actions para:

* Instalar dependências automaticamente
* Configurar ambiente de testes
* Executar todos os testes com Pytest
* Validar o projeto a cada Push ou Pull Request

---

## Exemplos de Endpoints

### Cadastro

POST /cadastro

```json
{
  "username": "luizfelipe",
  "password": "123456"
}
```

### Login

POST /login

```json
{
  "username": "luizfelipe",
  "password": "123456"
}
```

### Criar Produto

POST /produtos

```json
{
  "nome": "Notebook",
  "preco": 3500,
  "estoque": 10,
  "categoria": "Informática"
}
```

---

## Testes Implementados

* Teste de cadastro
* Teste de login
* Teste de criação de produto
* Teste de atualização
* Teste de exclusão
* Teste de busca
* Teste de produto inexistente
* Testes de validação
* Testes de autenticação

---

## Autor

Luiz Felipe

Estudante de Ciência da Computação - UFAM

GitHub:
https://github.com/LuizFelipe-bitmax

LinkedIn:
https://www.linkedin.com/
