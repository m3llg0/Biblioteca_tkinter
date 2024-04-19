import tkinter as tk
from bd import register
from bd import login
from conexao import connect

mydb = connect()

# Funções -----------------------------------------

def cadastrar():

    # Adicionando no Banco de Dados -------------
    def adicionando():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        data_nasc = entry_data_nasc.get()
        rua = entry_rua.get()
        bairro = entry_bairro.get()
        cidade = entry_cidade.get()
        estado = entry_estado.get()
        cep = entry_cep.get()

        janela2 = tk.Tk()
        janela2.title('Confirmação: ')
        janela2.geometry('500x500')
        cadastro = register(mydb, nome, email, senha, data_nasc, rua, bairro, cidade, estado, cep)

        label_cadastro = tk.Label(janela2, text='Usuário registrado com sucesso.')
        label_cadastro.pack()

        botao_continuar = tk.Button(janela2, text='Continuar', command=inicio)
        botao_continuar.pack()

    # Janela principal do cadastro -----------------------------
    janela_cadastro = tk.Tk()
    janela_cadastro.title("Faça aqui o seu Cadastro")
    janela_cadastro.geometry('500x500')

    label_titulo = tk.Label(janela_cadastro, text="Faça aqui seu Cadastro: ")
    label_titulo.pack()

    # Nome ------------------------------------
    label_nome = tk.Label(janela_cadastro, text="Nome: ")
    label_nome.pack()
    entry_nome = tk.Entry(janela_cadastro)
    entry_nome.pack()

    # Email -------------------------------------
    label_email = tk.Label(janela_cadastro, text="Email: ")
    label_email.pack()
    entry_email = tk.Entry(janela_cadastro)
    entry_email.pack()

    # Senha -------------------------------------
    label_senha = tk.Label(janela_cadastro, text="Senha: ")
    label_senha.pack()
    entry_senha = tk.Entry(janela_cadastro, show="*")
    entry_senha.pack()

    # Data de Nascimento ------------------------------
    label_data_nasc = tk.Label(janela_cadastro, text="Data de Nascimento: ")
    label_data_nasc.pack()
    entry_data_nasc = tk.Entry(janela_cadastro)
    entry_data_nasc.pack()

    # Rua ---------------------------------------
    label_rua = tk.Label(janela_cadastro, text="Rua: ")
    label_rua.pack()
    entry_rua = tk.Entry(janela_cadastro)
    entry_rua.pack()

    # Bairro ------------------------------------
    label_bairro = tk.Label(janela_cadastro, text="Bairro: ")
    label_bairro.pack()
    entry_bairro = tk.Entry(janela_cadastro)
    entry_bairro.pack()

    # Cidade ------------------------------------
    label_cidade = tk.Label(janela_cadastro, text="Cidade: ")
    label_cidade.pack()
    entry_cidade = tk.Entry(janela_cadastro)
    entry_cidade.pack()

    # Estado ------------------------------------
    label_estado = tk.Label(janela_cadastro, text="Estado: ")
    label_estado.pack()
    entry_estado = tk.Entry(janela_cadastro)
    entry_estado.pack()

    # CEP ------------------------------------
    label_cep = tk.Label(janela_cadastro, text="CEP: ")
    label_cep.pack()
    entry_cep = tk.Entry(janela_cadastro)
    entry_cep.pack()

    # Botões ------------------------------------
    botao_cadastrar = tk.Button(janela_cadastro, text= "Cadastrar", command=adicionando)
    botao_cadastrar.pack()

    botao_voltar = tk.Button(janela_cadastro, text = "Cancelar", command=janela_cadastro.destroy)
    botao_voltar.pack()

def entrar():
    janela_login = tk.Tk()
    janela_login.title('Login')
    janela_login.geometry('500x500')
    label_titulo = tk.Label(janela_login, text="Login")
    label_titulo.pack()

    # Email -------------------------------------
    label_email = tk.Label(janela_login, text="Email: ")
    label_email.pack()
    entry_email = tk.Entry(janela_login)
    entry_email.pack()

    # Senha -------------------------------------
    label_senha = tk.Label(janela_login, text="Senha: ")
    label_senha.pack()
    entry_senha = tk.Entry(janela_login, show="*")
    entry_senha.pack()

    # Logando -----------------------------------
    email = entry_email.get()
    senha = entry_senha.get()

    logando = login(mydb, email, senha)

    botao_entrar = tk.Button(janela_login, text='Entrar', command=inicio)
    botao_entrar.pack()

    botao_voltar = tk.Button(janela_login, text = "Cancelar", command=janela_login.destroy)
    botao_voltar.pack()

def inicio():
    janela_home = tk.Tk()
    janela_home.title('Home')
    janela_home.geometry('500x500')

    label_titulo = tk.Label(janela_home, text='Biblioteca Fênix')
    label_titulo.pack()

    label_welcome = tk.Label(janela_home, text='Seja bem vindo(a)!')
    label_welcome.pack()

    label_espaco = tk.Label(janela_home, text=' ')
    label_espaco.pack()

    botao_cadastrol = tk.Button(janela_home, text='Cadastrar Livro', command=cadastro_livro)
    botao_cadastrol.pack()

    botao_update = tk.Button(janela_home, text='Atualizar Livro', command=atualizar_livro)
    botao_update.pack()

    botao_listar = tk.Button(janela_home, text='Listar livros', command=listar)
    botao_listar.pack()

    botao_emprestar = tk.Button(janela_home, text='Emprestar Livro', command=emprestar)
    botao_emprestar.pack()

    botao_devolver = tk.Button(janela_home, text='Devolver Livro', command=devolver)
    botao_devolver.pack()

    



janela_principal = tk.Tk()
janela_principal.title('Biblioteca Fênix')
janela_principal.geometry('500x500')

label_principal = tk.Label(janela_principal, text='Biblioteca Fênix')
label_principal.pack()

label_escolha = tk.Label(janela_principal, text='Escolha:')
label_escolha.pack()

botao_entrar = tk.Button(janela_principal, text='Entrar', command=entrar)
botao_entrar.pack()

botao_cadastro = tk.Button(janela_principal, text='Cadastrar-se', command=cadastrar)
botao_cadastro.pack()

botao_fechar = tk.Button(janela_principal, text = "Fechar", command=janela_principal.destroy)
botao_fechar.pack()


janela_principal.mainloop()