import tkinter as tk
from tkinter import messagebox
import sqlite3

class CadastroVenda(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(pady=20)

        labelTitulo = tk.Label(self, text="Cadastro de Venda", font=("Arial", 16))
        labelTitulo.pack(pady=10)

        tk.Label(self, text="Produto:").pack(pady=5)
        self.entradaProduto = tk.Entry(self)
        self.entradaProduto.pack(pady=5)

        tk.Label(self, text="Quantidade:").pack(pady=5)
        self.entradaQuantidade = tk.Entry(self)
        self.entradaQuantidade.pack(pady=5)

        tk.Label(self, text="Valor:").pack(pady=5)
        self.entradaValor = tk.Entry(self)
        self.entradaValor.pack(pady=5)

        self.botaoCadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrarVenda)
        self.botaoCadastrar.pack(pady=10)

        self.conexao = sqlite3.connect('vendas.db')
        self.criar_tabela()

    def criar_tabela(self):
        with self.conexao:
            self.conexao.execute('''
                CREATE TABLE IF NOT EXISTS vendas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    produto TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    valor REAL NOT NULL
                )
            ''')

    def cadastrarVenda(self):
        produto = self.entradaProduto.get()
        quantidade = self.entradaQuantidade.get()
        valor = self.entradaValor.get()

        if produto == "" or quantidade == "" or valor == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            with self.conexao:
                self.conexao.execute('''
                    INSERT INTO vendas (produto, quantidade, valor) VALUES (?, ?, ?)
                ''', (produto, int(quantidade), float(valor)))
            messagebox.showinfo("Sucesso", "Venda cadastrada com sucesso!")
            self.limparCampos()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar: {e}")

    def limparCampos(self):
        self.entradaProduto.delete(0, tk.END)
        self.entradaQuantidade.delete(0, tk.END)
        self.entradaValor.delete(0, tk.END)
