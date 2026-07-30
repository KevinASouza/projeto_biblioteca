import os
from flask import Flask
from controllers.LivroController import livro_bp
from controllers.UsuarioController import usuario_bp
from dotenv import load_dotenv

app = Flask(__name__)

app.secret_key = os.getenv('CHAVE')

app.register_blueprint(livro_bp)
app.register_blueprint(usuario_bp)

load_dotenv()

chave = os.getenv('SSL_PRIVATE_KEY')
certificado = os.getenv('SSL_CERTIFICATION')


if __name__ == '__main__':
    app.run(
        debug=True,
        host='localhost',
        port=8000,
        ssl_context=(certificado, chave)
    )