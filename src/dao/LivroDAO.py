from models.Livro import Livro
from dataBase.Connection import session

class LivroDAO:

    @staticmethod
    def inserir_livro(livro: Livro):
        session.add(livro)
        session.commit()
        return livro

    @staticmethod
    def listar_livros():
        livros = session.query(Livro).all()
        return livros