from flask import render_template, request, redirect, Blueprint, session, flash, url_for
from dao.UsuarioDAO import UsuarioDAO
from models.Usuario import Usuario
from werkzeug.security import generate_password_hash


usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/cadastroUsuario', methods=['POST'])
def adicionar_usuario():
    dados = request.form

    usuario = Usuario(
        id=None,
        nome=dados['nome'],
        apelido=dados['apelido'],
        senha=generate_password_hash(dados['senha'])
    )

    UsuarioDAO.inserir_usuario(usuario)

    flash(f'{usuario.apelido} adicionado(a) com sucesso!')

    return redirect(url_for('livro.get_formulario'))


@usuario_bp.route('/formularioCadastroUsuario', methods=['GET'])
def get_form_cadastro():
    return render_template('usuario/formCadastroUsuario.html', titulo='Cadastro de Usuario')

@usuario_bp.route('/login', methods=['GET'])
def login():
    proxima = request.args.get('proxima') # Capturando a variável passada na URL
    return render_template('usuario/formLogin.html', titulo='Login', proxima=proxima)


@usuario_bp.route('/autenticar', methods=['POST'])
def autenticar():
    dados = request.form
    if UsuarioDAO.get_usuario(dados.get('apelido'), dados.get('senha')) is not None:
        usuario = session['usuario'] = request.form.get('apelido')
        flash(f'{usuario} logado com sucesso!')
        ppg = request.form.get('proxima') # Pegando a variável passada do forms à rota.
        return redirect(ppg)
    else:
        flash('Usuário ou senha estão incorretos!')
        return redirect(url_for('livro.get_formulario'))


@usuario_bp.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('livro.get_formulario'))
