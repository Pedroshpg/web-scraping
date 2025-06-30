import requests

class Login:
    def __init__(self,login,senha):
        self.login = login
        self.senha = senha

    def fazer_login(self):
        link = "https://quotes.toscrape.com/login"
        sessao = requests.Session()
        dados_login = { 
            "username" : self.login, 
            "password" : self.senha
        }
        resultado = sessao.post(link, data=dados_login)
        return resultado