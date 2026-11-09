import datetime
from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Session, select
from app.database import engine, get_session
from app.models import Agendamento, Barbeiro
from app.security import gerar_senha_hash

app = FastAPI(title="Barbearia Alfa Concept - Core Engine")

@app.on_event("startup")
def on_startup():
    """ Executado ao iniciar o servidor. Cria as tabelas necessárias no banco
    de dados e popula um barbeiro administrador padrão de testes se a tabela estiver vazia. """
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        if not session.exec(select(Barbeiro)).first():
            teste_barbeiro = Barbeiro(
                nome="Marcus Vinicius", 
                email="marcus@alfa.com", 
                senha_hash=gerar_senha_hash("admin123")
            )
            session.add(teste_barbeiro)
            session.commit()

@app.post("/agendamentos/", response_model=Agendamento)
def criar_agendamento(agendamento: Agendamento, session: Session = Depends(get_session)):
    """ Endpoint para criação de agendamento autônomo. Aplica a regra de negócio
    crítica de validação para impedir a colisão física de horários no banco. """
    # Consulta se já existe um agendamento idêntico para o mesmo barbeiro no mesmo dia e hora
    query = select(Agendamento).where(
        Agendamento.barbeiro_id == agendamento.barbeiro_id,
        Agendamento.data_hora == agendamento.data_hora
    )
    conflito = session.exec(query).first()
    
    if conflito:
        # Se houver conflito, rejeita a requisição e retorna o erro HTTP 400
        raise HTTPException(status_code=400, detail="Colisao de horarios! Vaga ja preenchida.")
        
    session.add(agendamento)
    session.commit()
    session.refresh(agendamento)
    return agendamento

@app.get("/agendamentos/{barbeiro_id}")
def listar_agenda_diaria(barbeiro_id: int, session: Session = Depends(get_session)):
    """ Endpoint restrito para o painel administrativo do barbeiro consultar
    cronologicamente os seus compromissos registrados. """
    query = select(Agendamento).where(Agendamento.barbeiro_id == barbeiro_id)
    return session.exec(query).all()


