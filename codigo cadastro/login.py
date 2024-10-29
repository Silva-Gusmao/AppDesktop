import tkinter as tk
from tkinter import messagebox
from telaPrincipal import abrirTelaPrincipal

def validarLogin(entradaUsuario, entradaSenha, janelaLogin):
    usuario = entradaUsuario.get()
    senha = entradaSenha.get()

    if usuario == "" or senha == "":
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")
        return

    if usuario == "ney" and senha == "123":
        janelaLogin.destroy()
        abrirTelaPrincipal()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

def centralizarJanela(janela, largura, altura):
    telaLargura = janela.winfo_screenwidth()
    telaAltura = janela.winfo_screenheight()
    x = (telaLargura // 2) - (largura // 2)
    y = (telaAltura // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def IniciarLogin():
    janelaLogin = tk.Tk()
    janelaLogin.title("Tela de Login - Senai")

    labelUsuario = tk.Label(janelaLogin, text="Login:")
    labelUsuario.pack(pady=5)
    entradaUsuario = tk.Entry(janelaLogin)
    entradaUsuario.pack(pady=5)

    labelSenha = tk.Label(janelaLogin, text="Senha:")
    labelSenha.pack(pady=5)
    entradaSenha = tk.Entry(janelaLogin, show="*")
    entradaSenha.pack(pady=5)

    botaologin = tk.Button(janelaLogin, text="Login", command=lambda: validarLogin(entradaUsuario, entradaSenha, janelaLogin))
    botaologin.pack(pady=20)

    centralizarJanela(janelaLogin, 300, 200)
    janelaLogin.mainloop()
