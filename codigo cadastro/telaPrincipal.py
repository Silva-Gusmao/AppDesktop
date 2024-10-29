import tkinter as tk
from cadastro.cadastroUsuario import CadastroUsuario
from cadastro.cadastroCliente import FrameCliente
from cadastro.cadastroProduto import FrameProduto
from cadastro.cadastroCidade import CadastroCidade
from cadastro.cadastrovendas import CadastroVenda
from cadastro.cadastroTipodePagamento import CadastroTipoPagamento
from PIL import Image, ImageTk

def abrirTelaPrincipal():
    global janelaPrincipal, frameConteudo
    janelaPrincipal = tk.Tk()
    janelaPrincipal.title("Growth Supplements")
    janelaPrincipal.state('zoomed')

    menuPrincipal = tk.Menu(janelaPrincipal)

    menuCadastro = tk.Menu(menuPrincipal, tearoff=0)
    menuCadastro.add_command(label="USUÁRIOS", command=abrirCadastroUsuarios)
    menuCadastro.add_command(label="CLIENTES", command=abrirCadastroClientes)
    menuCadastro.add_command(label="PRODUTOS", command=abrirCadastroProdutos)
    menuCadastro.add_command(label="CIDADES", command=abrirCadastroCidades)
    menuCadastro.add_command(label="VENDAS", command=abrirCadastroVendas)
    menuCadastro.add_command(label="TIPOS DE PAGAMENTO", command=abrirCadastroTiposPagamento)
    menuPrincipal.add_cascade(label="CADASTRAR", menu=menuCadastro)

    menuRelatorios = tk.Menu(menuPrincipal, tearoff=0)
    menuRelatorios.add_command(label="Relatório de Vendas", command=abrirRelatorioVendas)
    menuRelatorios.add_command(label="Relatório de Estoque", command=abrirRelatorioEstoque)
    menuPrincipal.add_cascade(label="RELATÓRIOS", menu=menuRelatorios)

    menuConfigurações = tk.Menu(menuPrincipal, tearoff=0)
    menuConfigurações.add_command(label="Configurações Gerais", command=abrirConfiguracoes)
    menuPrincipal.add_cascade(label="CONFIGURAÇÕES", menu=menuConfigurações)

    menuAjuda = tk.Menu(menuPrincipal, tearoff=0)
    menuAjuda.add_command(label="Sobre", command=abrirSobre)
    menuPrincipal.add_cascade(label="AJUDA", menu=menuAjuda)

    janelaPrincipal.config(menu=menuPrincipal)

    frameConteudo = tk.Frame(janelaPrincipal)
    frameConteudo.pack(fill="both", expand=True)

    labelTitulo = tk.Label(janelaPrincipal, text="Bem-vindo à Growft", font=("Arial", 24, "bold"))
    labelTitulo.pack(pady=10)

    labelBemVindo = tk.Label(janelaPrincipal, text="Bem-vindo ao sistema!", font=("Arial", 16))
    labelBemVindo.pack(pady=20)

    imagem = Image.open(r"neymarrr.jpg")
    imagem = imagem.resize((600, 500))
    imagemTk = ImageTk.PhotoImage(imagem)

    labelImagem = tk.Label(janelaPrincipal, image=imagemTk)
    labelImagem.image = imagemTk
    labelImagem.pack(pady=150)

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

def abrirCadastroCidades():
    limparConteudo()
    frame = CadastroCidade(frameConteudo)
    frame.pack(fill="both", expand=True)

def abrirCadastroVendas():
    limparConteudo()
    frame = CadastroVenda(frameConteudo)
    frame.pack(fill="both", expand=True)

def abrirCadastroTiposPagamento():
    limparConteudo()
    frame = CadastroTipoPagamento(frameConteudo)
    frame.pack(fill="both", expand=True)

def abrirRelatorioVendas():
    limparConteudo()
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
