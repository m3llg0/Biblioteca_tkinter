import tkinter as tk
from bd import *
from bd import register, login, inserir, update, listar, emprestar, devolver
from conexao import connect
from tkinter import *

mydb = connect()

# Cadastrar V
def cadastrar():

    # Adicionando no Banco de Dados --
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
    
        cadastrando = register(mydb, nome, email, senha, data_nasc, rua, bairro, cidade, estado, cep)

    # Janela principal do cadastro -----------------------------
    janela_cadastro = tk.Tk()
    janela_cadastro.title("Faça aqui o seu Cadastro")
    janela_cadastro.geometry('500x250')
    janela_cadastro.configure(background='black')

    label_titulo = tk.Label(janela_cadastro, text="Faça aqui seu Cadastro: ", background='black', foreground='white')
    label_titulo.grid(column=2, row=0)
    label_titulo.configure(font=("Courier", 12, "bold"))

    # Nome ------------------------------------
    label_nome = tk.Label(janela_cadastro, text="Nome: ", background='black', foreground='white')
    label_nome.grid(column=1, row=1)
    entry_nome = tk.Entry(janela_cadastro)
    entry_nome.grid(column=1, row=2)

    # Email -------------------------------------
    label_email = tk.Label(janela_cadastro, text="Email: ", background='black', foreground='white')
    label_email.grid(column=1, row=3)
    entry_email = tk.Entry(janela_cadastro)
    entry_email.grid(column=1, row=4)

    # Senha -------------------------------------
    label_senha = tk.Label(janela_cadastro, text="Senha: ", background='black', foreground='white')
    label_senha.grid(column=1, row=5)
    entry_senha = tk.Entry(janela_cadastro, show="*")
    entry_senha.grid(column=1, row=6)

    # Data de Nascimento ------------------------------
    label_data_nasc = tk.Label(janela_cadastro, text="Data de Nascimento: ", background='black', foreground='white')
    label_data_nasc.grid(column=2, row=1)
    entry_data_nasc = tk.Entry(janela_cadastro)
    entry_data_nasc.grid(column=2, row=2)

    # Rua ---------------------------------------
    label_rua = tk.Label(janela_cadastro, text="Rua: ", background='black', foreground='white')
    label_rua.grid(column=2, row=3)
    entry_rua = tk.Entry(janela_cadastro)
    entry_rua.grid(column=2, row=4)

    # Bairro ------------------------------------
    label_bairro = tk.Label(janela_cadastro, text="Bairro: ", background='black', foreground='white')
    label_bairro.grid(column=2, row=5)
    entry_bairro = tk.Entry(janela_cadastro)
    entry_bairro.grid(column=2, row=6)

    # Cidade ------------------------------------
    label_cidade = tk.Label(janela_cadastro, text="Cidade: ", background='black', foreground='white')
    label_cidade.grid(column=3, row=1)
    entry_cidade = tk.Entry(janela_cadastro)
    entry_cidade.grid(column=3, row=2)

    # Estado ------------------------------------
    label_estado = tk.Label(janela_cadastro, text="Estado: ", background='black', foreground='white')
    label_estado.grid(column=3, row=3)
    entry_estado = tk.Entry(janela_cadastro)
    entry_estado.grid(column=3, row=4)

    # CEP ------------------------------------
    label_cep = tk.Label(janela_cadastro, text="CEP: ", background='black', foreground='white')
    label_cep.grid(column=3, row=5)
    entry_cep = tk.Entry(janela_cadastro)
    entry_cep.grid(column=3, row=6)
    
    # Botões ------------------------------------
    label_vazio1 = tk.Label(janela_cadastro, text='', background='black')
    label_vazio1.grid(column=1, row=8)

    botao_cadastrar = tk.Button(janela_cadastro, text= "Cadastrar", command=adicionando)
    botao_cadastrar.grid(column=1, row=9)

    label_vazio2 = tk.Label(janela_cadastro, text='', background='black')
    label_vazio2.grid(column=2, row=8)

    botao_voltar = tk.Button(janela_cadastro, text = "Continuar", command=inicio)
    botao_voltar.grid(column=2, row=9)

    label_vazio3 = tk.Label(janela_cadastro, text='', background='black')
    label_vazio3.grid(column=3, row=8)

    botao_voltar = tk.Button(janela_cadastro, text = "Cancelar", command=janela_cadastro.destroy)
    botao_voltar.grid(column=3, row=9)

# Login V
def entrar():
    janela_login = tk.Tk()
    janela_login.title('Login')
    janela_login.geometry('500x250')
    janela_login.configure(background='black')

    label_titulo = tk.Label(janela_login, text="Faça o seu login:", background='black', foreground='white')
    label_titulo.grid(column=2, row=1)
    label_titulo.configure(font=("Courier", 12, "bold"))

    # Email -------------------------------------
    label_email = tk.Label(janela_login, text="Email: ", background='black', foreground='white')
    label_email.grid(column=2, row=2)
    entry_email = tk.Entry(janela_login)
    entry_email.grid(column=2, row=3)

    # Senha -------------------------------------
    label_senha = tk.Label(janela_login, text="Senha: ", background='black', foreground='white')
    label_senha.grid(column=2, row=4)
    entry_senha = tk.Entry(janela_login, show="*")
    entry_senha.grid(column=2, row=5)

    # Logando -----------------------------------
    email = entry_email.get()
    senha = entry_senha.get()

    logando = login(mydb, email, senha)

    label_vazio = tk.Label(janela_login, text='                                    ', background='black')
    label_vazio.grid(column=0, row=0)

    label_vazio1 = tk.Label(janela_login, text='', background='black')
    label_vazio1.grid(column=1, row=6)

    botao_entrar = tk.Button(janela_login, text=' Entrar ', command=inicio)
    botao_entrar.grid(column=1, row=7)

    label_vazio2 = tk.Label(janela_login, text='', background='black')
    label_vazio2.grid(column=3, row=6)

    botao_voltar = tk.Button(janela_login, text = "Cancelar", command=janela_login.destroy)
    botao_voltar.grid(column=3, row=7)

# Cadastro de Livros
def cadastro_livro():
    def adicionando_l():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        ano = entry_ano.get()
        status = 1

        janela_cl = tk.Tk()
        janela_cl.title('Confirmação: ')
        janela_cl.geometry('500x250')
        janela_cl.configure(background='black')
        cadastro_l = inserir(mydb, titulo, autor, ano, status)

        label_cadastro = tk.Label(janela_cl, text='Livro registrado com sucesso.', background='black', foreground='white')
        label_cadastro.grid(column=0, row=1)

        botao_voltar = tk.Button(janela_cl, text = "Voltar", command=janela_cl.destroy)
        botao_voltar.grid(column=0, row=2)
    
    # Janela principal    
    janela_cl = tk.Tk()
    janela_cl.title('Cadastro do Livro')
    janela_cl.geometry('500x250')
    janela_cl.configure(background='black')


    label_nome = tk.Label(janela_cl, text='Cadastrar Livro', background='black', foreground='white')
    label_nome.grid(column=2, row=0)
    label_nome.configure(font=("Courier", 12, "bold"))

    # Titulo
    label_titulo = tk.Label(janela_cl, text='Título: ', background='black', foreground='white')
    label_titulo.grid(column=1, row=2)
    entry_titulo = tk.Entry(janela_cl)
    entry_titulo.grid(column=1, row=3)

    # Autor
    label_autor = tk.Label(janela_cl, text='Autor: ', background='black', foreground='white')
    label_autor.grid(column=2, row=2)
    entry_autor = tk.Entry(janela_cl)
    entry_autor.grid(column=2, row=3)

    # Ano
    label_ano = tk.Label(janela_cl, text='Ano: ', background='black', foreground='white')
    label_ano.grid(column=3, row=2)
    entry_ano = tk.Entry(janela_cl)
    entry_ano.grid(column=3, row=3)

    # Botões
    botao_cadastrar = tk.Button(janela_cl, text= "Cadastrar", command=adicionando_l)
    botao_cadastrar.grid(column=1, row=5)

    botao_voltar = tk.Button(janela_cl, text = "Cancelar", command=janela_cl.destroy)
    botao_voltar.grid(column=3, row=5)

# Atualização do livro
def update_livro():
    def update_l():
        titulo_antigo = entry_ta.get()
        titulo_novo = entry_tn.get()
        autor_novo = entry_autorn.get()
        ano_novo = entry_anon.get()
        status_novo = entry_statusn.get()

        janela_up2 = tk.Tk()
        janela_up2.title('Confirmação: ')
        janela_up2.geometry('500x500')
        atualizando = update(mydb, titulo_antigo, titulo_novo, autor_novo, ano_novo, status_novo)

        label_conf = tk.Label(janela_up2, text='Livro atualizado com sucesso.')
        label_conf.pack()

        botao_voltar = tk.Button(janela_up2, text = "Voltar", command=janela_up2.destroy)
        botao_voltar.pack()
    
    # Janela principal    
    janela_up = tk.Tk()
    janela_up.title('Atualização do Livro')
    janela_up.geometry('500x500')

    label_nome = tk.Label(janela_up, text='Atualizar Livro')
    label_nome.pack()

    # Titulo Antigo
    label_ta = tk.Label(janela_up, text='Digite o título do livro que deseja atualizar: ')
    label_ta.pack()
    entry_ta = tk.Entry(janela_up)
    entry_ta.pack()

    # Título Novo
    label_tn = tk.Label(janela_up, text='Digite o novo título: ')
    label_tn.pack()
    entry_tn = tk.Entry(janela_up)
    entry_tn.pack()

    # Novo autor
    label_autorn = tk.Label(janela_up, text='Digite o novo autor: ')
    label_autorn.pack()
    entry_autorn = tk.Entry(janela_up)
    entry_autorn.pack()

    # Novo ano
    label_anon = tk.Label(janela_up, text='Digite o novo ano: ')
    label_anon.pack()
    entry_anon = tk.Entry(janela_up)
    entry_anon.pack()

    # Novo status
    label_statusn = tk.Label(janela_up, text='Digite o novo status (1 para Disponível, 0 para Indisponível):')
    label_statusn.pack()
    entry_statusn = tk.Entry(janela_up)
    entry_statusn.pack()

    # Botões
    botao_up = tk.Button(janela_up, text= "Atualizar", command=update_l)
    botao_up.pack()

    botao_voltar = tk.Button(janela_up, text = "Cancelar", command=janela_up.destroy)
    botao_voltar.pack()

# Listar os Livros
def listar_livros():
    livros = []

    janela_listar = tk.Tk()
    janela_listar.title("Lista de Livros")
    janela_listar.geometry('500x500')
    label_title = tk.Label(janela_listar, text='Lista de Livros')
    label_title.pack()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    for livro in livros:
        texto = f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}"
        label_lista = tk.Label(janela_listar, text=texto)
        label_lista.pack()

    mydb.close()

    botao_voltar = tk.Button(janela_listar, text = "Voltar", command=janela_listar.destroy)
    botao_voltar.pack()
  
# Emprestar Livros
def emprestar_livro():
    def mudando_em():
        id_livro = entry_id.get()
        emprestando = emprestar(mydb, id_livro)

    janela_em = tk.Tk()
    janela_em.title("Página de emprestar um livro")
    
    text_emprestar = tk.Label(janela_em, text="Emprestar um livro!")
    text_emprestar.grid(column=0, row=2, padx= 10, pady=10)

    text_id = tk.Label(janela_em,text= "Digite o id do livro:")
    text_id.grid(column=0,row=3, padx= 10, pady=10)
    entry_id = tk.Entry(janela_em)
    entry_id.grid(column=0, row=4, padx= 10, pady=10)

    botao_voltar6 = tk.Button(janela_em, text="Fechar a janela", command= janela_em.destroy)
    botao_voltar6.grid(column=0, row=1, padx=10, pady=10)

    botao_entrar6 = tk.Button(janela_em, text="Concluido!", command=mudando_em)
    botao_entrar6.grid(column=0, row=7,  padx= 10, pady=10)

# Devolver livros
def devolver_livro():
    def mudando():
        id_livro = entry_id.get()
        devolvendo = devolver(mydb, id_livro)

    janela_dev = tk.Toplevel()
    janela_dev.title("Página de devolver um livro")
    
    text_emprestar = tk.Label(janela_dev, text="Devolver um livro!")
    text_emprestar.grid(column=0, row=2, padx= 10, pady=10)

    text_id = tk.Label(janela_dev,text= "Digite o id do livro:")
    text_id.grid(column=0,row=3, padx= 10, pady=10)
    entry_id = tk.Entry(janela_dev)
    entry_id.grid(column=0, row=4, padx= 10, pady=10)

    botao_voltar6 = tk.Button(janela_dev, text="Fechar a janela", command= janela_dev.destroy)
    botao_voltar6.grid(column=0, row=1, padx=10, pady=10)

    botao_entrar6 = tk.Button(janela_dev, text="Concluido!", command=mudando)
    botao_entrar6.grid(column=0, row=7,  padx= 10, pady=10)

# Home V 
def inicio():
    janela_home = tk.Tk()
    janela_home.title('Home')
    janela_home.geometry('500x250')
    janela_home.configure(background='black')

    label_titulo = tk.Label(janela_home, text='Biblioteca Fênix', background='black', foreground='white')
    label_titulo.grid(column=2, row=0)
    label_titulo.configure(font=("Courier", 16, "bold"))

    label_welcome = tk.Label(janela_home, text='Escolha a opção desejada: ', background='black', foreground='white')
    label_welcome.grid(column=2, row=1)

    label_espaco = tk.Label(janela_home, text=' ', background='black', foreground='white')
    label_espaco.grid(column=2, row=2)

    botao_cadastrol = tk.Button(janela_home, text='Cadastrar Livro', command=cadastro_livro)
    botao_cadastrol.grid(column=1, row=3)

    botao_update = tk.Button(janela_home, text='Atualizar Livro', command=update_livro)
    botao_update.grid(column=1, row=5)

    botao_listar = tk.Button(janela_home, text='Listar livros', command=listar_livros)
    botao_listar.grid(column=2, row=4)

    botao_emprestar = tk.Button(janela_home, text='Emprestar Livro', command=emprestar_livro)
    botao_emprestar.grid(column=3, row=3)

    botao_devolver = tk.Button(janela_home, text='Devolver Livro', command=devolver_livro)
    botao_devolver.grid(column=3, row=5)

    label_vazio = tk.Label(janela_home, text='             ', background='black')
    label_vazio.grid(column=0, row=0)

    label_vazio2 = tk.Label(janela_home, text='  ', background='black')
    label_vazio2.grid(column=2, row=7)

    label_vazio3 = tk.Label(janela_home, text='  ', background='black')
    label_vazio3.grid(column=2, row=9)

    botao_fechar = tk.Button(janela_home, text = "Fechar", command=janela_home.destroy)
    botao_fechar.grid(column=2, row=10)


# Janela Principal ----------------------------
janela_principal = tk.Tk()
janela_principal.title('Biblioteca Portal Literário')
janela_principal.geometry('500x250')
janela_principal.configure(background='black')

label_principal = tk.Label(janela_principal, text='Biblioteca Portal Literário', background='black', foreground='white')
label_principal.grid(column=2, row=0)
label_principal.configure(font=("Courier", 16, "bold"))

label_vazio = tk.Label(janela_principal, text='         ', background='black')
label_vazio.grid(column=0, row=0)


label_escolha = tk.Label(janela_principal, text='Seja bem vindo(a)!', background='black', foreground='white')
label_escolha.grid(column=2, row=2)

label_vazio1 = tk.Label(janela_principal, text='', background='black')
label_vazio1.grid(column=2, row=3)

botao_entrar = tk.Button(janela_principal, text='     Entrar     ', command=entrar)
botao_entrar.grid(column=2, row=4)

label_vazio2 = tk.Label(janela_principal, text='    ', background='black')
label_vazio2.grid(column=2, row=5)

botao_cadastro = tk.Button(janela_principal, text='Cadastrar-se', command=cadastrar)
botao_cadastro.grid(column=2, row=6)

label_vazio3 = tk.Label(janela_principal, text='', background='black')
label_vazio3.grid(column=2, row=8)

botao_fechar = tk.Button(janela_principal, text = "Fechar", command=janela_principal.destroy)
botao_fechar.grid(column=3, row=10)


janela_principal.mainloop()