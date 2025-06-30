from classes import Login

login = input("Informe o Login:" )
senha = input("Informe a Senha:")

login_bot = Login(login, senha)
resultado = login_bot.fazer_login()

if "logout" in resultado.text.lower() or "sair" in resultado.text.lower():
    print("--Login realizado com sucesso!--")

#código opcional para fins de depuração: 
    with open("resposta_login.html", "w", encoding="utf-8") as f:
        f.write(resultado.text)

else:
    print("--Login ou senha inválida!--")


