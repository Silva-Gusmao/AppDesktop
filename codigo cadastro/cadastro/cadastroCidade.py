import tkinter as tk
from tkinter import messagebox
import sqlite3

class CadastroCidade(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(pady=20)

        labelTitulo = tk.Label(self, text="Cadastro de Cidade", font=("Arial", 16))
        labelTitulo.pack(pady=10)

        tk.Label(self, text="Nome da Cidade:").pack(pady=5)
        self.entradaNome = tk.Entry(self)
        self.entradaNome.pack(pady=5)

        tk.Label(self, text="Estado:").pack(pady=5)
        self.entradaEstado = tk.Entry(self)
        self.entradaEstado.pack(pady=5)

        self.botaoCadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrarCidade)
        self.botaoCadastrar.pack(pady=10)

        self.conexao = sqlite3.connect('cidades.db')
        self.criar_tabela()

    def criar_tabela(self):
        with self.conexao:
            self.conexao.execute('''
                CREATE TABLE IF NOT EXISTS cidades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    estado TEXT NOT NULL
                )
            ''')

    def cadastrarCidade(self):
        nome = self.entradaNome.get()
        estado = self.entradaEstado.get()

        if nome == "" or estado == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            with self.conexao:
                self.conexao.execute('''
                    INSERT INTO cidades (nome, estado) VALUES (?, ?)
                ''', (nome, estado))
            messagebox.showinfo("Sucesso", "Cidade cadastrada com sucesso!")
            self.limparCampos()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar: {e}")

    def limparCampos(self):
        self.entradaNome.delete(0, tk.END)
        self.entradaEstado.delete(0, tk.END)
