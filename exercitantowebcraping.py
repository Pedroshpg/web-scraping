import requests

link = "https://quotes.toscrape.com/login"

sessao = requests.session()

dados_login = {
                
                "username" : "pedronoleto2018@hotmail.com",
                "password" : "password",           
              }

resultado = sessao.post(link, data=dados_login)

#código opcional para fins de depuração: 
with open("resposta_login.html", "w", encoding="utf-8") as f:
    f.write(resultado.text)
#--

if "logout" in resultado.text.lower() or "sair" in resultado.text.lower():
    print("--Login realizado com sucesso!--")
else:
    print("--Falha no login!--")


