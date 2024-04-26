import tkinter as tk
from bd import register, login, inserir, update, emprestar, devolver
from conexao import connect
from tkinter import *

mydb = connect()

# Cadastrar
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

    # Janela Cadastro 
    janela_cadastro = tk.Tk()
    janela_cadastro.title("Faça aqui o seu Cadastro")
    janela_cadastro.geometry('500x250')
    janela_cadastro.configure(background='black')

    label_titulo = tk.Label(janela_cadastro, text="Faça aqui seu Cadastro: ", background='black', foreground='white')
    label_titulo.grid(column=2, row=0)
    label_titulo.configure(font=("Courier", 12, "bold"))

    # Nome --
    label_nome = tk.Label(janela_cadastro, text="Nome: ", background='black', foreground='white')
    label_nome.grid(column=1, row=1)
    entry_nome = tk.Entry(janela_cadastro)
    entry_nome.grid(column=1, row=2)

    # Email --
    label_email = tk.Label(janela_cadastro, text="Email: ", background='black', foreground='white')
    label_email.grid(column=1, row=3)
    entry_email = tk.Entry(janela_cadastro)
    entry_email.grid(column=1, row=4)

    # Senha --
    label_senha = tk.Label(janela_cadastro, text="Senha: ", background='black', foreground='white')
    label_senha.grid(column=1, row=5)
    entry_senha = tk.Entry(janela_cadastro, show="*")
    entry_senha.grid(column=1, row=6)

    # Data de Nascimento --
    label_data_nasc = tk.Label(janela_cadastro, text="Data de Nascimento: ", background='black', foreground='white')
    label_data_nasc.grid(column=2, row=1)
    entry_data_nasc = tk.Entry(janela_cadastro)
    entry_data_nasc.grid(column=2, row=2)

    # Rua --
    label_rua = tk.Label(janela_cadastro, text="Rua: ", background='black', foreground='white')
    label_rua.grid(column=2, row=3)
    entry_rua = tk.Entry(janela_cadastro)
    entry_rua.grid(column=2, row=4)

    # Bairro --
    label_bairro = tk.Label(janela_cadastro, text="Bairro: ", background='black', foreground='white')
    label_bairro.grid(column=2, row=5)
    entry_bairro = tk.Entry(janela_cadastro)
    entry_bairro.grid(column=2, row=6)

    # Cidade --
    label_cidade = tk.Label(janela_cadastro, text="Cidade: ", background='black', foreground='white')
    label_cidade.grid(column=3, row=1)
    entry_cidade = tk.Entry(janela_cadastro)
    entry_cidade.grid(column=3, row=2)

    # Estado --
    label_estado = tk.Label(janela_cadastro, text="Estado: ", background='black', foreground='white')
    label_estado.grid(column=3, row=3)
    entry_estado = tk.Entry(janela_cadastro)
    entry_estado.grid(column=3, row=4)

    # CEP --
    label_cep = tk.Label(janela_cadastro, text="CEP: ", background='black', foreground='white')
    label_cep.grid(column=3, row=5)
    entry_cep = tk.Entry(janela_cadastro)
    entry_cep.grid(column=3, row=6)
    
    # Botões --
    botao_cadastrar = tk.Button(janela_cadastro, text= "Cadastrar", command=adicionando)
    botao_cadastrar.grid(column=1, row=9)

    botao_voltar = tk.Button(janela_cadastro, text = "Continuar", command=inicio)
    botao_voltar.grid(column=2, row=9)

    botao_voltar = tk.Button(janela_cadastro, text = "Cancelar", command=janela_cadastro.destroy)
    botao_voltar.grid(column=3, row=9)

    # Espaços vazios --
    label_vazio = tk.Label(janela_cadastro, text='', background='black')
    label_vazio.grid(column=1, row=8)

    label_vazio1 = tk.Label(janela_cadastro, text='', background='black')
    label_vazio1.grid(column=2, row=8)

    label_vazio2 = tk.Label(janela_cadastro, text='', background='black')
    label_vazio2.grid(column=3, row=8)

# Login 
def entrar():
    janela_login = tk.Tk()
    janela_login.title('Login')
    janela_login.geometry('500x250')
    janela_login.configure(background='black')

    label_titulo = tk.Label(janela_login, text="Faça o seu login:", background='black', foreground='white')
    label_titulo.grid(column=2, row=1)
    label_titulo.configure(font=("Courier", 12, "bold"))

    # Email --
    label_email = tk.Label(janela_login, text="Email: ", background='black', foreground='white')
    label_email.grid(column=2, row=2)
    entry_email = tk.Entry(janela_login)
    entry_email.grid(column=2, row=3)

    # Senha --
    label_senha = tk.Label(janela_login, text="Senha: ", background='black', foreground='white')
    label_senha.grid(column=2, row=4)
    entry_senha = tk.Entry(janela_login, show="*")
    entry_senha.grid(column=2, row=5)

    # Logando --
    email = entry_email.get()
    senha = entry_senha.get()

    logando = login(mydb, email, senha)

    # Botões --
    botao_entrar = tk.Button(janela_login, text=' Entrar ', command=inicio)
    botao_entrar.grid(column=1, row=7)

    botao_voltar = tk.Button(janela_login, text = "Cancelar", command=janela_login.destroy)
    botao_voltar.grid(column=3, row=7)

    # Espaços vazios --
    label_vazio = tk.Label(janela_login, text='                                    ', background='black')
    label_vazio.grid(column=0, row=0)

    label_vazio1 = tk.Label(janela_login, text='', background='black')
    label_vazio1.grid(column=1, row=6)

    label_vazio2 = tk.Label(janela_login, text='', background='black')
    label_vazio2.grid(column=3, row=6)

# Cadastro de Livros 
def cadastro_livro():
    # Adicionando no Banco de Dados --
    def adicionando_l():
        titulo = entry_nome.get()
        autor = entry_autor.get()
        ano = entry_ano.get()
        status = 1

        cadastro_l = inserir(mydb, titulo, autor, ano, status)

    # Janela principal -- 
    janela_cadastro_livro = tk.Tk()
    janela_cadastro_livro.title('Cadastro do Livro')
    janela_cadastro_livro.geometry('500x250')
    janela_cadastro_livro.configure(background='black')


    label_titulo = tk.Label(janela_cadastro_livro, text='Cadastrar Livro', background='black', foreground='white')
    label_titulo.grid(column=2, row=0)
    label_titulo.configure(font=("Courier", 12, "bold"))

    # Titulo --
    label_nome = tk.Label(janela_cadastro_livro, text='Título: ', background='black', foreground='white')
    label_nome.grid(column=1, row=2)
    entry_nome = tk.Entry(janela_cadastro_livro)
    entry_nome.grid(column=1, row=3)

    # Autor --
    label_autor = tk.Label(janela_cadastro_livro, text='Autor: ', background='black', foreground='white')
    label_autor.grid(column=2, row=2)
    entry_autor = tk.Entry(janela_cadastro_livro)
    entry_autor.grid(column=2, row=3)


    # Ano --
    label_ano = tk.Label(janela_cadastro_livro, text='Ano: ', background='black', foreground='white')
    label_ano.grid(column=3, row=2)
    entry_ano = tk.Entry(janela_cadastro_livro)
    entry_ano.grid(column=3, row=3)

    # Botões
    botao_cadastrar = tk.Button(janela_cadastro_livro, text= "Cadastrar", command=adicionando_l)
    botao_cadastrar.grid(column=1, row=5)

    botao_voltar = tk.Button(janela_cadastro_livro, text = "Voltar", command=janela_cadastro_livro.destroy)
    botao_voltar.grid(column=3, row=5)

    # Espaços vazios --
    label_vazio = tk.Label(janela_cadastro_livro, text="", background='black', foreground='white')
    label_vazio.grid(column=1, row=4)

    label_vazio2 = tk.Label(janela_cadastro_livro, text="", background='black', foreground='white')
    label_vazio2.grid(column=3, row=4)
    
    label_vazio3 = tk.Label(janela_cadastro_livro, text="             ", background='black', foreground='white')
    label_vazio3.grid(column=0, row=0)

# Atualização do livro
def update_livro():
    # Mundando no Banco de Dados --
    def atualizar_livro():
        titulo_antigo = entry_titulo_antigo.get()
        titulo_novo = entry_titulo_novo.get()
        autor_novo = entry_autor_novo.get()
        ano_novo = entry_ano_novo.get()
        status_novo = entry_status_novo.get()

        atualizando = update(mydb, titulo_antigo, titulo_novo, autor_novo, ano_novo, status_novo)
    
    # Janela principal --
    janela_up = tk.Tk()
    janela_up.title('Atualização do Livro')
    janela_up.geometry('500x250')
    janela_up.configure(background='black')

    label_nome = tk.Label(janela_up, text='Atualizar Livro', background='black', foreground='white')
    label_nome.grid(column=2, row=0)
    label_nome.configure(font=("Courier", 12, "bold"))

    # Titulo Antigo --
    label_titulo_antigo = tk.Label(janela_up, text='Digite o título do', background='black', foreground='white')
    label_titulo_antigo.grid(column=2, row=2)
    label_titulo_antigo2 = tk.Label(janela_up, text='livro que deseja atualizar: ', background='black', foreground='white')
    label_titulo_antigo2.grid(column=2, row=3)
    entry_titulo_antigo = tk.Entry(janela_up)
    entry_titulo_antigo.grid(column=2, row=4)

    # Título Novo --
    label_titulo_novo = tk.Label(janela_up, text='Digite o novo título: ', background='black', foreground='white')
    label_titulo_novo.grid(column=1, row=2)
    entry_titulo_novo = tk.Entry(janela_up)
    entry_titulo_novo.grid(column=1, row=3)

    # Novo autor --
    label_autor_novo = tk.Label(janela_up, text='Digite o novo autor: ', background='black', foreground='white')
    label_autor_novo.grid(column=1, row=4)
    entry_autor_novo = tk.Entry(janela_up)
    entry_autor_novo.grid(column=1, row=5)

    # Novo ano --
    label_ano_novo = tk.Label(janela_up, text='Digite o novo ano: ', background='black', foreground='white')
    label_ano_novo.grid(column=3, row=4)
    entry_ano_novo = tk.Entry(janela_up)
    entry_ano_novo.grid(column=3, row=5)

    # Novo status --
    label_status_novo = tk.Label(janela_up, text='Digite o novo status', background='black', foreground='white')
    label_status_novo.grid(column=3, row=2)
    entry_status_novo = tk.Entry(janela_up)
    entry_status_novo.grid(column=3, row=3)

    # Botões --
    botao_up = tk.Button(janela_up, text= "Atualizar", command=atualizar_livro)
    botao_up.grid(column=1, row=10)

    botao_voltar = tk.Button(janela_up, text = "Cancelar", command=janela_up.destroy)
    botao_voltar.grid(column=3, row=10)
    
    # Espaços vazios -- 
    label_vazio = tk.Label(janela_up, text="", background='black')
    label_vazio.grid(column=1, row=9)

    label_vazio2 = tk.Label(janela_up, text="", background='black')
    label_vazio2.grid(column=2, row=9)

    label_vazio3 = tk.Label(janela_up, text="             ", background='black')
    label_vazio3.grid(column=0, row=0)

# Listar os Livros V
def listar_livros():
    livros = []

    janela_listar = tk.Tk()
    janela_listar.title("Lista de Livros")
    janela_listar.geometry('500x250')
    janela_listar.configure(background='black')

    label_title = tk.Label(janela_listar, text='Lista de Livros', background='black', foreground='white')
    label_title.pack()
    label_title.configure(font=("Courier", 12, "bold"))

    # Puxando do Banco de Dados --
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    # Exibindo a lista --
    for livro in livros:
        texto = f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}"
        label_lista = tk.Label(janela_listar, text=texto, background='black', foreground='white')
        label_lista.pack()

    mydb.close()

    botao_voltar = tk.Button(janela_listar, text = "Voltar", command=janela_listar.destroy)
    botao_voltar.pack()
  
# Emprestar Livros
def emprestar_livro():
    # Mudando no Banco de Dados -- 
    def mudando_em():
        id_livro = entry_id.get()
        emprestando = emprestar(mydb, id_livro)
    
    # Janela de empréstimo
    janela_emprestimo = tk.Tk()
    janela_emprestimo.title("Emprestar um livro")
    janela_emprestimo.geometry('500x250')
    janela_emprestimo.configure(background='black')
    
    label_emprestar = tk.Label(janela_emprestimo, text="Emprestar um livro", background='black', foreground='white')
    label_emprestar.grid(column=2, row=0)
    label_emprestar.configure(font=("Courier", 12, "bold"))

    # ID --
    label_id = tk.Label(janela_emprestimo,text= "Digite o id do livro:", background='black', foreground='white')
    label_id.grid(column=2,row=3)
    entry_id = tk.Entry(janela_emprestimo)
    entry_id.grid(column=2, row=4)

    # Botões --
    botao_voltar6 = tk.Button(janela_emprestimo, text="Cancelar", command= janela_emprestimo.destroy)
    botao_voltar6.grid(column=3, row=6)

    botao_entrar6 = tk.Button(janela_emprestimo, text="Concluido!", command=mudando_em)
    botao_entrar6.grid(column=1, row=6)

    # Espaços vazios -- 
    label_vazio = tk.Label(janela_emprestimo, text="", background='black')
    label_vazio.grid(column=2, row=5)

    label_vazio2 = tk.Label(janela_emprestimo, text='         ', background='black')
    label_vazio2.grid(column=0, row=0)

    label_vazio3 = tk.Label(janela_emprestimo, text='                               ', background='black')
    label_vazio3.grid(column=0, row=6)

# Devolver livros
def devolver_livro():
    # Mudando no Banco de Dados
    def mudando():
        id_livro = entry_id.get()
        devolvendo = devolver(mydb, id_livro)

    # Janela de devolução
    janela_devolucao = tk.Tk()
    janela_devolucao.title("Devolução de livro")
    janela_devolucao.geometry('500x250')
    janela_devolucao.configure(background='black')
    
    label_devolucao = tk.Label(janela_devolucao, text="Devolver um livro", background='black', foreground='white')
    label_devolucao.grid(column=2, row=0)
    label_devolucao.configure(font=("Courier", 12, "bold"))

    # ID --
    label_id = tk.Label(janela_devolucao,text= "Digite o id do livro:", background='black', foreground='white')
    label_id.grid(column=2, row=1)
    entry_id = tk.Entry(janela_devolucao)
    entry_id.grid(column=2, row=2)

    # Botões --
    botao_voltar = tk.Button(janela_devolucao, text="Fechar", command= janela_devolucao.destroy)
    botao_voltar.grid(column=3, row=7)

    botao_entrar = tk.Button(janela_devolucao, text="Concluido", command=mudando)
    botao_entrar.grid(column=1, row=7)

    # Espaços vazios
    label_vazio = tk.Label(janela_devolucao, text='                               ', background='black')
    label_vazio.grid(column=0, row=7)

    label_vazio1 = tk.Label(janela_devolucao, text='    ', background='black')
    label_vazio1.grid(column=3, row=3)

    label_vazio2 = tk.Label(janela_devolucao, text='    ', background='black')
    label_vazio2.grid(column=1, row=3)

# Home
def inicio():
    # Janela de início
    janela_home = tk.Tk()
    janela_home.title('Home')
    janela_home.geometry('500x250')
    janela_home.configure(background='black')

    label_titulo = tk.Label(janela_home, text='Biblioteca Fênix', background='black', foreground='white')
    label_titulo.grid(column=2, row=0)
    label_titulo.configure(font=("Courier", 16, "bold"))

    label_welcome = tk.Label(janela_home, text='Escolha a opção desejada: ', background='black', foreground='white')
    label_welcome.grid(column=2, row=1)

    # Botões --
    label_espaco = tk.Label(janela_home, text=' ', background='black', foreground='white')
    label_espaco.grid(column=2, row=2)

    botao_cadastro_livro = tk.Button(janela_home, text='Cadastrar Livro', command=cadastro_livro)
    botao_cadastro_livro.grid(column=1, row=3)

    botao_update = tk.Button(janela_home, text='Atualizar Livro', command=update_livro)
    botao_update.grid(column=1, row=5)

    botao_listar = tk.Button(janela_home, text='Listar livros', command=listar_livros)
    botao_listar.grid(column=2, row=4)

    botao_emprestar = tk.Button(janela_home, text='Emprestar Livro', command=emprestar_livro)
    botao_emprestar.grid(column=3, row=3)

    botao_devolver = tk.Button(janela_home, text='Devolver Livro', command=devolver_livro)
    botao_devolver.grid(column=3, row=5)

    botao_fechar = tk.Button(janela_home, text = "Fechar", command=janela_home.destroy)
    botao_fechar.grid(column=2, row=10)

    # Espaços vazios --
    label_vazio = tk.Label(janela_home, text='             ', background='black')
    label_vazio.grid(column=0, row=0)

    label_vazio2 = tk.Label(janela_home, text='  ', background='black')
    label_vazio2.grid(column=2, row=7)

    label_vazio3 = tk.Label(janela_home, text='  ', background='black')
    label_vazio3.grid(column=2, row=9)


# Janela Principal ----------------------------
janela_principal = tk.Tk()
janela_principal.title('Biblioteca Portal Literário')
janela_principal.geometry('500x250')
janela_principal.configure(background='black')

# Textos --
label_titulo = tk.Label(janela_principal, text='Biblioteca Portal Literário', background='black', foreground='white')
label_titulo.grid(column=2, row=0)
label_titulo.configure(font=("Courier", 16, "bold"))

label_welcome = tk.Label(janela_principal, text='Seja bem vindo(a)!', background='black', foreground='white')
label_welcome.grid(column=2, row=2)

botao_entrar = tk.Button(janela_principal, text='     Entrar     ', command=entrar)
botao_entrar.grid(column=2, row=4)

# Botões --
botao_cadastro = tk.Button(janela_principal, text='Cadastrar-se', command=cadastrar)
botao_cadastro.grid(column=2, row=6)

botao_fechar = tk.Button(janela_principal, text = "Fechar", command=janela_principal.destroy)
botao_fechar.grid(column=3, row=10)

# Espaços vazios --
label_vazio = tk.Label(janela_principal, text='         ', background='black')
label_vazio.grid(column=0, row=0)

label_vazio1 = tk.Label(janela_principal, text='', background='black')
label_vazio1.grid(column=2, row=3)

label_vazio2 = tk.Label(janela_principal, text='    ', background='black')
label_vazio2.grid(column=2, row=5)

label_vazio3 = tk.Label(janela_principal, text='', background='black')
label_vazio3.grid(column=2, row=8)

janela_principal.mainloop()