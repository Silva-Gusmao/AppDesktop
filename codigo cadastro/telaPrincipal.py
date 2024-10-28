import tkinter as tk
from cadastros.cadastroUsuario import CadastroUsuario
from cadastros.cadastroCliente import FrameCliente
from cadastros.cadastroProduto import FrameProduto

def abrirTelaPrincipal():
    global janelaPrincipal, frameConteudo
    janelaPrincipal = tk.Tk()
    janelaPrincipal.title("Tela Principal")
    janelaPrincipal.state('zoomed')

    # Criação do menu principal
    menuPrincipal = tk.Menu(janelaPrincipal)

    # Menu cadastro
    menuCadastro = tk.Menu(menuPrincipal, tearoff=0)
    menuCadastro.add_command(label="USUÁRIOS", command=abrirCadastroUsuarios)
    menuCadastro.add_command(label="CLIENTES", command=abrirCadastroClientes)
    menuCadastro.add_command(label="PRODUTOS", command=abrirCadastroProdutos)
    menuPrincipal.add_cascade(label="CADASTRAR", menu=menuCadastro)

    # Menu Relatórios (exemplo)
    menuRelatorios = tk.Menu(menuPrincipal, tearoff=0)
    menuRelatorios.add_command(label="Relatório de Vendas", command=abrirRelatorioVendas)
    menuRelatorios.add_command(label="Relatório de Estoque", command=abrirRelatorioEstoque)
    menuPrincipal.add_cascade(label="RELATÓRIOS", menu=menuRelatorios)

    # Menu Configurações (exemplo)
    menuConfigurações = tk.Menu(menuPrincipal, tearoff=0)
    menuConfigurações.add_command(label="Configurações Gerais", command=abrirConfiguracoes)
    menuPrincipal.add_cascade(label="CONFIGURAÇÕES", menu=menuConfigurações)

    # Menu Ajuda (exemplo)
    menuAjuda = tk.Menu(menuPrincipal, tearoff=0)
    menuAjuda.add_command(label="Sobre", command=abrirSobre)
    menuPrincipal.add_cascade(label="AJUDA", menu=menuAjuda)

    janelaPrincipal.config(menu=menuPrincipal)

    # Frame de conteúdo
    frameConteudo = tk.Frame(janelaPrincipal)
    frameConteudo.pack(fill="both", expand=True)

    # Iniciar o mainloop da janela
    janelaPrincipal.mainloop()

def abrirCadastroUsuarios():
    limparConteudo()
    frame = CadastroUsuario(frameConteudo)
    frame.pack(fill="both", expand=True)

def abrirCadastroClientes():
    limparConteudo()
    frame = FrameCliente(frameConteudo)
    frame.pack(fill="both", expand=True)

def abrirCadastroProdutos():
    limparConteudo()
    frame = FrameProduto(frameConteudo)
    frame.pack(fill="both", expand=True)

def abrirRelatorioVendas():
    limparConteudo()  # Adicionamos a limpeza aqui
    tk.Label(frameConteudo, text="Relatório de Vendas").pack()

def abrirRelatorioEstoque():
    limparConteudo()
    tk.Label(frameConteudo, text="Relatório de Estoque").pack()

def abrirSobre():
    limparConteudo()
    tk.Label(frameConteudo, text="Sobre o Sistema").pack()

def abrirConfiguracoes():
    limparConteudo()
    tk.Label(frameConteudo, text="Configurações Gerais").pack()

def limparConteudo():
    for widget in frameConteudo.winfo_children():
        widget.destroy()
