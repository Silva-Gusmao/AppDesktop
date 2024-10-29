import tkinter as tk
from tkinter import messagebox
import sqlite3

class FrameCliente(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(pady=20)

        tk.Label(self, text="Cadastro de Cliente", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Nome do Cliente:").pack(pady=5)
        self.entradaNomeCliente = tk.Entry(self)
        self.entradaNomeCliente.pack(pady=5)

        tk.Label(self, text="E-mail:").pack(pady=5)
        self.entradaEmail = tk.Entry(self)
        self.entradaEmail.pack(pady=5)

        tk.Label(self, text="Telefone:").pack(pady=5)
        self.entradaTelefone = tk.Entry(self)
        self.entradaTelefone.pack(pady=5)

        tk.Button(self, text="Cadastrar", command=self.cadastrarCliente).pack(pady=10)

        self.conexao = sqlite3.connect('clientes.db')
        self.criar_tabela()

    def criar_tabela(self):
        with self.conexao:
            self.conexao.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone TEXT NOT NULL
                )
            ''')

    def cadastrarCliente(self):
        nome = self.entradaNomeCliente.get()
        email = self.entradaEmail.get()
        telefone = self.entradaTelefone.get()

        if nome == "" or email == "" or telefone == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            with self.conexao:
                self.conexao.execute('''
                    INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)
                ''', (nome, email, telefone))
            messagebox.showinfo("Sucesso", f"Cliente \"{nome}\" cadastrado com sucesso!")
            self.limparCampos()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar: {e}")

    def limparCampos(self):
        self.entradaNomeCliente.delete(0, tk.END)
        self.entradaEmail.delete(0, tk.END)
        self.entradaTelefone.delete(0, tk.END)

# Para testar o FrameCliente isoladamente (opcional)
if __name__ == "__main__":
    root = tk.Tk()
    FrameCliente(root)
    root.mainloop()
