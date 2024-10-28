import tkinter as tk
from tkinter import messagebox
import sqlite3

class CadastroUsuario(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(pady=20)

        labeltitulo = tk.Label(self, text="Cadastro de Usuário", font=("Arial", 16))
        labeltitulo.pack(pady=10)

        tk.Label(self, text="Login:").pack(pady=5)
        self.entradaLogin = tk.Entry(self)
        self.entradaLogin.pack(pady=5)

        tk.Label(self, text="Senha:").pack(pady=5)
        self.entradaSenha = tk.Entry(self, show="*")
        self.entradaSenha.pack(pady=5)

        tk.Label(self, text="Nome:").pack(pady=5)
        self.entradaNome = tk.Entry(self)
        self.entradaNome.pack(pady=5)

        self.botaoCadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrarUsuario)
        self.botaoCadastrar.pack(pady=10)

        self.conexao = sqlite3.connect('usuarios.db')
        self.criar_tabela()

    def criar_tabela(self):
        with self.conexao:
            self.conexao.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    nome TEXT NOT NULL
                )
            ''')

    def cadastrarUsuario(self):
        nome = self.entradaNome.get()
        login = self.entradaLogin.get()
        senha = self.entradaSenha.get()

        if login == "" or senha == "" or nome == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            with self.conexao:
                self.conexao.execute('''
                    INSERT INTO usuarios (login, senha, nome) VALUES (?, ?, ?)
                ''', (login, senha, nome))
            messagebox.showinfo("Sucesso", f"Usuário \"{nome}\" cadastrado com sucesso!")
            self.limparCampos()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar: {e}")

    def limparCampos(self):
        self.entradaLogin.delete(0, tk.END)
        self.entradaSenha.delete(0, tk.END)
        self.entradaNome.delete(0, tk.END)
