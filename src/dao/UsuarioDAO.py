from models.Usuario import Usuario
from dataBase.Connection import session2
from sqlalchemy import select
from werkzeug.security import check_password_hash

class UsuarioDAO:

    @staticmethod
    def inserir_usuario(usuario: Usuario):
        session2.add(usuario)
        session2.commit()

        return usuario

    @staticmethod
    def get_usuario(apelido: str, senha: str):

        stmt = select(Usuario).where(Usuario.apelido == apelido)
        usuario = session2.execute(stmt).scalar_one_or_none()

        if usuario and check_password_hash(usuario.senha, senha):
            return usuario

        return None
