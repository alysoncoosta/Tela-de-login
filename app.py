from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulação de um usuário no banco de dados (apenas para exemplo)
USUARIOS = {
    "usuario1": {"senha": "senha1"},
    "email@email.com": {"senha": "outrasenha"}
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome_ou_email = request.form['nome_ou_email']
        senha = request.form['senha']

        if nome_ou_email in USUARIOS and USUARIOS[nome_ou_email]['senha'] == senha:
            # Login bem-sucedido, você pode redirecionar para outra página
            return redirect(url_for('pagina_protegida'))
        else:
            # Login falhou, renderize novamente o formulário com uma mensagem de erro
            return render_template('login.html', erro="Nome/E-mail ou senha incorretos")

    # Se a requisição for GET, apenas exibe o formulário de login
    return render_template('login.html', erro=None)

@app.route('/pagina_protegida')
def pagina_protegida():
    return "<h1>Você está logado!</h1>"

@app.route('/esqueci_senha', methods=['GET', 'POST'])
def esqueci_senha():
    if request.method == 'POST':
        email_ou_nome = request.form['email_ou_nome']
        # Aqui você precisará implementar a lógica para:
        # 1. Buscar o usuário no banco de dados pelo e-mail ou nome.
        # 2. Gerar um token único.
        # 3. Salvar o token no banco de dados associado ao usuário.
        # 4. Enviar um e-mail com um link contendo o token.
        # Por enquanto, vamos apenas exibir uma mensagem.
        return f"Um link de redefinição de senha foi enviado para {email_ou_nome} (funcionalidade não implementada)."
    return render_template('esqueci_senha.html')

if __name__ == '__main__':
    app.run(debug=True)