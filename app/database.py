import os
from sqlmodel import create_engine, Session

# Configuração da URL de conexão com o banco de dados
# Em ambiente de testes ou se a variável não estiver no sistema, usa um banco SQLite local padrão
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")

# Criação do motor de conexão (Engine) do banco de dados relacional
# O parâmetro check_same_thread=False é exigido especificamente quando o SQLite é acionado em testes locais
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

def get_session():
    """ Fornece uma sessão aberta do banco de dados para os controladores e garante
    o fechamento automático do recurso após a conclusão do ciclo de requisição. """
    with Session(engine) as session:
        yield session

