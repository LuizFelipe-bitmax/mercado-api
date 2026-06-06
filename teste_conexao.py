from database.connection import engine

try:
    conexao = engine.connect()

    print("Conectado com sucesso!")

    conexao.close()

except Exception as erro:
    print("Erro:", erro)