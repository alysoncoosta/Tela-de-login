# Tela de Login Flask em Python

Este projeto é uma tela de login simples desenvolvida utilizando o framework Flask em Python. O objetivo é fornecer uma base para autenticação de usuários em aplicações web.

## Funcionalidades Atuais

* **Interface de Login:** Uma página web com campos para nome de usuário/e-mail e senha, além de um botão de "Entrar".
* **Estilização:** A página de login é estilizada com CSS (arquivo `style.css` na pasta `static`).
* **Funcionalidade "Esqueceu a senha":**
    * Um link/botão "Esqueceu a senha?" na página de login.
    * Uma página separada (`/esqueci_senha`) onde o usuário pode inserir seu e-mail ou nome de usuário para solicitar a redefinição da senha.
    * Mensagens de feedback (`mensagem_info.html`, `mensagem_erro.html`) para informar o usuário sobre o status da solicitação de redefinição.


## Próximos Passos (A Fazer)

* **Banco de Dados:** Configuração para utilizar o banco de dados MySQL com o Flask-SQLAlchemy.
    * Definição de um modelo `Usuario` com campos para `id`, `nome`, `email`, `senha_hash`, `reset_token` e `reset_token_expiration`.
    * Criação da tabela `usuario` no banco de dados MySQL (se não existir).
* **Implementação Completa do "Esqueceu a senha":**
    * Envio de e-mails contendo o link de redefinição com o token gerado.
    * Criação de uma rota para verificar o token e exibir um formulário para o usuário inserir uma nova senha.
    * Lógica para atualizar a senha no banco de dados e invalidar o token.
* **Autenticação de Usuários:**
    * Implementar a lógica para verificar as credenciais do usuário (consultar o banco de dados e comparar a senha com o hash armazenado).
    * Gerenciamento de sessão para manter o usuário logado após o login bem-sucedido.
* **Registro de Novos Usuários:**
    * Criar uma página de registro.
    * Implementar a lógica para adicionar novos usuários ao banco de dados (lembrando de fazer o hash da senha antes de salvar).
* **Segurança:**
    * Implementar hashing seguro de senhas (por exemplo, usando `bcrypt`).
    * Validação de entrada para prevenir ataques.
    * Considerar o uso de HTTPS.
* **Testes:** Adicionar testes unitários e de integração para garantir a funcionalidade e a robustez da aplicação.
* **Melhorias na Interface:** Aprimorar o design e a experiência do usuário.

## Como Executar o Projeto (Desenvolvimento)

1.  **Certifique-se de ter o Python instalado.**
2.  **Instale as dependências:**
    ```bash
    pip install Flask Flask-SQLAlchemy mysqlclient
    ```
3.  **Configure o banco de dados MySQL:**
    * Crie um banco de dados com o nome especificado na configuração do `app.py`.
    * Crie um usuário com as permissões necessárias para acessar o banco de dados.
    * Atualize a URI de conexão no `app.py` com suas credenciais do MySQL.
4.  **Execute a aplicação Flask:**
    ```bash
    python app.py
    ```
5.  **Acesse a tela de login no seu navegador:** `http://127.0.0.1:5000/`
