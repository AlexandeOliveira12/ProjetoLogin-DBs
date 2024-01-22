from hashlib import md5
import re

NomeUsuario = input("insira seu nome de usuario -> ")

email_digitado = None  # Inicializa a variável para armazenar o email digitado

# Loop para garantir que o email seja válido
while True:
    Email = input("Insira seu email -> ")

    # Expressão regular para validar o formato do e-mail
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Verifica se o e-mail corresponde ao padrão
    if re.match(padrao_email, Email):
        print("Email válido!")
        email_digitado = Email  # Armazena o email digitado
        break  # Sai do loop se o email for válido
    else:
        print("Formato de email inválido. Por favor, insira um email válido.")

senha_correta = None  # Inicializa a variável para armazenar a senha correta

# Loop para garantir que as senhas coincidam
while True:
    Senha = input("\nInsira uma senha -> ")
    ConfirmSenha = input("\nPor favor, confirme sua senha -> ")

    # Verifica se as senhas são iguais
    if Senha == ConfirmSenha:
        print("Senha confirmada com sucesso!")
        senha_correta = Senha  # Armazena a senha correta
        break  # Sai do loop se as senhas são iguais
    else:
        print("\nAs senhas não coincidem. Por favor, tente novamente.")

SenhaHash = senha_correta.encode("utf8")
Hash = md5(SenhaHash).hexdigest()



