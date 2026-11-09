import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session
from app.main import app, get_session

# Configura um banco de dados em memória isolado e limpo exclusivamente para rodar a rodada de testes
engine_test = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})

def override_get_session():
    """ Substitui a sessão de produção por uma sessão isolada em memória """
    with Session(engine_test) as session:
        yield session

# Aplica a injeção de dependências do FastAPI para usar o banco de testes
app.dependency_overrides[get_session] = override_get_session
client = TestClient(app)

@pytest.fixture(autouse=True)
def run_around_tests():
    """ Garante que a estrutura das tabelas seja criada antes de cada teste
    e completamente destruída após a execução, isolando os cenários. """
    SQLModel.metadata.create_all(engine_test)
    yield
    SQLModel.metadata.drop_all(engine_test)

def test_deve_impedir_colisao_de_horarios():
    """ Teste de Integração Automatizado: Simula o fluxo central e comprova
    que o sistema rejeita um duplo agendamento no mesmo horário. """
    # Dados fictícios do agendamento comum inicial
    dados_reserva = {
        "barbeiro_id": 1,
        "nome_cliente": "Carlos Silva",
        "telefone_cliente": "11987654321",
        "data_hora": "2026-11-21T14:00:00"
    }
    
    # 1. A primeira tentativa de agendamento na vaga livre deve passar com sucesso (HTTP 200)
    response1 = client.post("/agendamentos/", json=dados_reserva)
    assert response1.status_code == 200
    
    # 2. TENTATIVA DE COLISÃO SIMULTÂNEA: Outro cliente tenta reservar exatamente a mesma vaga
    dados_colisao = {
        "barbeiro_id": 1,
        "nome_cliente": "Manoel Souza",
        "telefone_cliente": "11999998888",
        "data_hora": "2026-11-21T14:00:00"
    }
    response2 = client.post("/agendamentos/", json=dados_colisao)
    
    # O controlador do FastAPI deve obrigatoriamente interceptar, travar e retornar erro HTTP 400
    assert response2.status_code == 400
    assert response2.json()["detail"] == "Colisao de horarios! Vaga ja preenchida."


