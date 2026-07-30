# Projeto Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em Python e Flask para fins de estudo. A aplicação permite a autenticação de usuários e o gerenciamento de uma coleção de livros.

## Funcionalidades

*   **Autenticação de Usuário:** Cadastro e login para acesso ao sistema.
*   **Gerenciamento de Livros:** Listagem e adição de novos livros ao acervo.

## Tecnologias

*   **Linguagem:** Python
*   **Framework:** Flask
*   **Banco de Dados:** SQLite
*   **ORM:** SQLAlchemy
*   **Frontend:** HTML, Jinja2, Bootstrap

## Estrutura do Projeto

O projeto está organizado da seguinte forma dentro do diretório `src/`:

```
src/
├── dataBase/
│   ├── Connection.py       # Configuração da conexão com o banco
│   ├── gestao_livros.db    # Arquivo de banco de dados (criado na execução)
│   └── gestao_usuarios.db  # Arquivo de banco de dados (criado na execução)
├── dao/
│   ├── LivroDAO.py         # Camada de acesso aos dados de livros
│   └── UsuarioDAO.py       # Camada de acesso aos dados de usuários
├── models/
│   ├── Livro.py            # Modelo de dados para Livro
│   └── Usuario.py          # Modelo de dados para Usuário
├── templates/
│   ├── livro/
│   └── usuario/
└── app.py                  # Arquivo principal da aplicação
```

## Instalação

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/projeto_biblioteca.git
cd projeto_biblioteca
```

### 2. Criar e Ativar o Ambiente Virtual

É recomendado o uso de um ambiente virtual para isolar as dependências.


### 3. Criar uma pasta chamada `certs` dentro da pasta raiz (src) do projeto para armazenar a chave privada e o certificado digital. 

Esses dois arquivos são esseciais para a implementação do protocolo TLS.


### Aplicação construida sem a utilização de IA, pois visa colocar em prática o meu conhecimento nesse momento.