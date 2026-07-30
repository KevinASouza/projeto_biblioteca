from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Usuario(Base):

    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    apelido = Column(String)
    senha = Column(String)


    def __init__(self, id: None,  nome: str, apelido: str, senha: str):
        self.id = id
        self.nome = nome
        self.apelido = apelido
        self.senha = senha