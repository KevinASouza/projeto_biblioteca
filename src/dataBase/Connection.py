from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conn_livros = create_engine('sqlite:///./dataBase/gestao_livros.db')

Session = sessionmaker(bind=conn_livros)
session = Session()


conn_usuario = create_engine('sqlite:///./dataBase/gestao_usuarios.db')

Session2 = sessionmaker(bind=conn_usuario)
session2 = Session2()