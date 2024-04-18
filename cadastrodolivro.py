import tkinter as tk
from bd import insert
from conexao import connect

mydb = connect()

def cadastrar_livro():
    janela_clivro = tk.Tk()
    janela_clivro.title('Cadastro do livro')
    jaela_clivro.geometry('500x500')
    label_titulo = tk.label(janela_clivro, text="cadastre o livro")
    label_titulo.pack()

    # Titulo  --------------------------------
    label_titulo = tk.label(janela_clivro, text="Título: ")
    label_titulo.pack()
    entry_titulo = tk.Entry(janela_clivro)
    entry_titulo.pack()
    
    # Autor ----------------------------------
    label_autor = tk.label(janela_clivro, text="Autor: ")
    label_autor.pack()
    entry_autor = tk.Entry(janela_clivro)
    entry_autor.pack()

    # Data -----------------------------------
    label_ano_pub = tk.label(janela_clivro, text="Ano de publicação")
    lavel_ano_pub.pack()
    entry_ano_pub = tk.Entry(janela_clivro)



janela_clivro = tk.TK()
botao = tk.button

janela_clivro.mainloop()

