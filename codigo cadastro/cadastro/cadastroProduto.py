import tkinter as tk
from tkinter import messagebox
import sqlite3

class FrameProduto(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(pady=20)

        tk.Label(self, text="Cadastro de Produto", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Nome do Produto:").pack(pady=5)
        self.entradaNomeProduto = tk.Entry(self)
        self.entradaNomeProduto.pack(pady=5)

        tk.Label(self, text="Preço:").pack(pady=5)
        self.entradaPreco = tk.Entry(self)
        self.entradaPreco.pack(pady=5)

        tk.Button(self, text="Cadastrar", command=self.cadastrarProduto).pack(pady=10)

        self.conexao = sqlite3.connect('produtos.db')
        self.criar_tabela()

    def criar_tabela(self):
        with self.conexao:
            self.conexao.execute('''
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL
                )
            ''')

    def cadastrarProduto(self):
        nome = self.entradaNomeProduto.get()
        preco = self.entradaPreco.get()

        if nome == "" or preco == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            with self.conexao:
                self.conexao.execute('''
                    INSERT INTO produtos (nome, preco) VALUES (?, ?)
                ''', (nome, float(preco)))
            messagebox.showinfo("Sucesso", f"Produto \"{nome}\" cadastrado com sucesso!")
            self.limparCampos()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar: {e}")

    def limparCampos(self):
        self.entradaNomeProduto.delete(0, tk.END)
        self.entradaPreco.delete(0, tk.END)

# Para testar o FrameProduto isoladamente (opcional)
if __name__ == "__main__":
    root = tk.Tk()
    FrameProduto(root)
    root.mainloop()
