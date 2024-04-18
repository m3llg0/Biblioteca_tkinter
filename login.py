import tkinter as tk
from bd import login
from conexao import connect

mydb = connect()

def entrar():
    janela2 = tk.Toplevel()

def abrir_janela():
    janela4 = tk.Toplevel()
    janela4.title('Confirmação do Login')
    janela4.geometry('300x300')
    texto_login = tk.Label(janela4, text = "Confirmação Login")
    texto_login.grid(row=1, column=0, padx = 10, pady = 5)
    login1 = login()
    login1.grid(row=4, column=0, padx = 10, pady = 5)



def entra():
    janela3 = tk.Toplevel()
    janela3.title('Login do Usuário')
    janela3.geometry('450x300')
    texto_login = tk.Label(janela3, text = "Login do Usuário")
    texto_login.grid(row=1, column=0, padx = 10, pady = 5)

    # Email -----------------------------
    texto_email = tk.Label(janela3, text = "Email: ")
    texto_email.grid(column=0, row=3, padx = 10, pady = 5)
    E1 = tk.Entry(janela3)
    E1.grid(column=0, row=5, padx = 10, pady = 5)

    # Senha -----------------------------
    texto_senha = tk.Label(janela3, text = "Senha: ")
    texto_senha.grid(column=0, row=7, padx = 10, pady = 5)
    E2 = tk.Entry(janela3)
    E2.grid(column=0, row=9, padx = 10, pady = 5)

    # Obtendo --------------------------
    def obter():
        email = E1.get()
        senha = E2.get()

        

    # Botões ----------------------------
    botao_voltar = tk.Button(janela3, text = "Cancelar", command=janela3.destroy)
    botao_voltar.grid(row=11, column=0, padx = 10, pady = 5)

    botao_cont = tk.Button(janela3, text = "Salvar", command=obter)
    botao_cont.grid(row=13, column=0, padx = 10, pady = 5)


janela = tk.Tk()
janela.title('Início')
janela.geometry('500x500')
texto_inicio = tk.Label(janela, text = "Biblioteca Fênix")
texto_inicio.grid(column=0, row=0, padx = 10, pady = 10)

texto1 = tk.Label(janela, text = "Deseja se cadastrar ou fazer login?")
texto1.grid(column=0, row=3, padx = 10, pady = 10)

botao = tk.Button(janela, text="Login", command=entrar)
botao.grid(row=6, column=0, padx = 10, pady = 10)

janela.mainloop()