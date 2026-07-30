from flask import render_template, request, redirect, Blueprint, session, flash, url_for
from models.Livro import Livro
from dao.LivroDAO import LivroDAO


livro_bp = Blueprint('livro', __name__)


@livro_bp.route('/', methods=['GET'])
def index():
    return redirect(url_for('livro.get_formulario'))


@livro_bp.route('/livro', methods=['GET'])
def listar_livros():

    usuario = session.get('usuario')

    if usuario is None:
        frase = 'Login'
    else:
        frase = 'Logout'
    lista_livros = LivroDAO.listar_livros()
    return render_template('livro/listaLivros.html', livros=lista_livros, titulo='Biblioteca', mensagem=frase, logado=usuario)


@livro_bp.route('/formulario', methods=['GET'])
def get_formulario():
    if session.get('usuario') is None:
        return redirect(url_for('usuario.login', proxima=url_for('livro.get_formulario'))) # Utilizando Query Parameters
    return render_template('livro/formCadastroLivro.html', titulo='Cadastro')

@livro_bp.route('/cadastro', methods=['POST'])
def adicionar_livro():
    dados = request.form

    livro = Livro(
        id=None,
        titulo=dados['titulo'],
        autor=dados['autor'],
        ano=int(dados['ano']),
    )

    LivroDAO.inserir_livro(livro)

    flash(f'{livro.titulo} adicionado com sucesso à biblioteca!')

    return redirect(url_for('livro.get_formulario'))
