
from def_tkinter import cadastrar, entrar, cadastro_livro, update_livro, listar_livros, emprestar_livro, devolver_livro, inicio
import tkinter as tk


# Janela Principal ----------------------------
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