from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, UniqueConstraint

class Barbeiro(SQLModel, table=True):
    """ Entidade que mapeia os profissionais parceiros cadastrados no estabelecimento.
    O e-mail possui restrição de unicidade para evitar contas duplicadas. """
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str = Field(unique=True)
    senha_hash: str

class Agendamento(SQLModel, table=True):
    """ Entidade central do MVP que registra os compromissos. 
    Contém a regra estrutural restritiva unindo barbeiro_id e data_hora para
    impedir duplicidade de agendamentos para o mesmo profissional. """
    __table_args__ = (
        UniqueConstraint("barbeiro_id", "data_hora", name="unique_barbeiro_horario"),
    )
    
    id: Optional[int] = Field(default=None, primary_key=True)
    barbeiro_id: int = Field(foreign_key="barbeiro.id")
    nome_cliente: str
    telefone_cliente: str
    data_hora: datetime
    status_reserva: str = Field(default="Confirmado")


