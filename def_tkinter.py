import tkinter as tk
from bd import register, login, insert, update, listar, give_back, emprestar, devolver
from conexao import connect

mydb = connect()

# Cadastrar
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

# Login
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

# Cadastro de Livros
def cadastro_livro():
    def adicionando_l():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        ano = entry_ano.get()
        status = 1

        janela_cl = tk.Tk()
        janela_cl.title('Confirmação: ')
        janela_cl.geometry('500x500')
        cadastro_l = insert(mydb, titulo, autor, ano, status)

        label_cadastro = tk.Label(janela_cl, text='Livro registrado com sucesso.')
        label_cadastro.pack()

        botao_continuar = tk.Button(janela_cl, text='Voltar', command=inicio)
        botao_continuar.pack()
    
    # Janela principal    
    janela_cl = tk.Tk()
    janela_cl.title('Cadastro do Livro')
    janela_cl.geometry('500x500')

    label_nome = tk.Label(janela_cl, text='Cadastrar Livro')
    label_nome.pack()

    # Titulo
    label_titulo = tk.Label(janela_cl, text='Título: ')
    label_titulo.pack()
    entry_titulo = tk.Entry(janela_cl)
    entry_titulo.pack()

    # Autor
    label_autor = tk.Label(janela_cl, text='Autor: ')
    label_autor.pack()
    entry_autor = tk.Entry(janela_cl)
    entry_autor.pack()

    # Ano
    label_ano = tk.Label(janela_cl, text='Ano: ')
    label_ano.pack()
    entry_ano = tk.Entry(janela_cl)
    entry_ano.pack()

    # Botões
    botao_cadastrar = tk.Button(janela_cl, text= "Cadastrar", command=adicionando_l)
    botao_cadastrar.pack()

    botao_voltar = tk.Button(janela_cl, text = "Cancelar", command=janela_cl.destroy)
    botao_voltar.pack()

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

        botao_voltar = tk.Button(janela_up2, text='Voltar', command=inicio)
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
def listar_livro():
    janela_list = tk.Tk()
    janela_list.title('Listar Livros')
    janela_list.geometry('500x500')

    label_list = tk.Label(janela_list, text='Lista de livros')
    label_list.pack()

    lista = listar(mydb)
    label_livros = tk.LabelFrame(janela_list, bg=lista)
    label_list.pack()

    botao_voltar = tk.Button(janela_list, text = "Cancelar", command=janela_list.destroy)
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

# Home 
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

    botao_update = tk.Button(janela_home, text='Atualizar Livro', command=update_livro)
    botao_update.pack()

    botao_listar = tk.Button(janela_home, text='Listar livros', command=listar_livro)
    botao_listar.pack()

    botao_emprestar = tk.Button(janela_home, text='Emprestar Livro', command=emprestar_livro)
    botao_emprestar.pack()

    botao_devolver = tk.Button(janela_home, text='Devolver Livro', command=devolver_livro)
    botao_devolver.pack()