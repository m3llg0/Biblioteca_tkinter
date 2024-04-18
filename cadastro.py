import tkinter as tk
from bd import register
from conexao import connect

mydb = connect()

# Salvar dados

def cadastrar():
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

def inicio():
    janela3 = tk.Toplevel()
    janela3.geometry('500x500')
    janela3.geometry('300x300')


    


# Dados cadastrados

janela = tk.Tk()
janela.title("Faça aqui o seu Cadastro")
janela.geometry('500x500')

label_titulo = tk.Label(janela, text="Faça aqui seu Cadastro: ")
label_titulo.pack()

label_nome = tk.Label(janela, text="Nome: ")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_email = tk.Label(janela, text="Email: ")
label_email.pack()
entry_email = tk.Entry(janela)
entry_email.pack()

label_senha = tk.Label(janela, text="Senha: ")
label_senha.pack()
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

label_data_nasc = tk.Label(janela, text="Data de Nascimento: ")
label_data_nasc.pack()
entry_data_nasc = tk.Entry(janela)
entry_data_nasc.pack()

label_rua = tk.Label(janela, text="Rua: ")
label_rua.pack()
entry_rua = tk.Entry(janela)
entry_rua.pack()

label_bairro = tk.Label(janela, text="Bairro: ")
label_bairro.pack()
entry_bairro = tk.Entry(janela)
entry_bairro.pack()

label_cidade = tk.Label(janela, text="Cidade: ")
label_cidade.pack()
entry_cidade = tk.Entry(janela)
entry_cidade.pack()

label_estado = tk.Label(janela, text="Estado: ")
label_estado.pack()
entry_estado = tk.Entry(janela)
entry_estado.pack()

label_cep = tk.Label(janela, text="CEP: ")
label_cep.pack()
entry_cep = tk.Entry(janela)
entry_cep.pack()

botao_cadastrar = tk.Button(janela, text= "Cadastrar", command=cadastrar)
botao_cadastrar.pack()

botao_voltar = tk.Button(janela, text = "Cancelar", command=janela.destroy)
botao_voltar.pack()

janela.mainloop()