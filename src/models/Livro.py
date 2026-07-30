from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Livro(Base):

    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(String)
    ano = Column(String)

    def __init__(self, id: None, titulo: str, autor: str, ano: str):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano