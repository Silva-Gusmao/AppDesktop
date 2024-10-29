import tkinter as tk
from tkinter import messagebox
import sqlite3

class CadastroTipoPagamento(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(pady=20)

        labelTitulo = tk.Label(self, text="Cadastro de Tipo de Pagamento", font=("Arial", 16))
        labelTitulo.pack(pady=10)

        tk.Label(self, text="Tipo de Pagamento:").pack(pady=5)
        self.entradaTipo = tk.Entry(self)
        self.entradaTipo.pack(pady=5)

        self.botaoCadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrarTipoPagamento)
        self.botaoCadastrar.pack(pady=10)

        self.conexao = sqlite3.connect('tipos_pagamento.db')
        self.criar_tabela()

    def criar_tabela(self):
        with self.conexao:
            self.conexao.execute('''
                CREATE TABLE IF NOT EXISTS tipos_pagamento (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL
                )
            ''')

    def cadastrarTipoPagamento(self):
        tipo = self.entradaTipo.get()

        if tipo == "":
            messagebox.showwarning("Atenção", "Preencha o campo de tipo de pagamento.")
            return

        try:
            with self.conexao:
                self.conexao.execute('''
                    INSERT INTO tipos_pagamento (tipo) VALUES (?)
                ''', (tipo,))
            messagebox.showinfo("Sucesso", "Tipo de pagamento cadastrado com sucesso!")
            self.limparCampos()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar: {e}")

    def limparCampos(self):
        self.entradaTipo.delete(0, tk.END)
