import tkinter as tk
from produto import Produto
from estoque import Estoque

class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Controle de Estoque')

        self.estoque = Estoque()

        self.criar_widgets()

    def criar_widgets(self):
        # Label e Entry para o nome do produto
        tk.Label(self, text='Nome do produto:').grid(row=0, column=0)
        self.nome_produto_entry = tk.Entry(self)
        self.nome_produto_entry.grid(row=0, column=1)

        # Label e Entry para o tamanho do produto
        tk.Label(self, text='Tamanho do produto:').grid(row=1, column=0)
        self.tamanho_produto_entry = tk.Entry(self)
        self.tamanho_produto_entry.grid(row=1, column=1)

        # Label e Entry para o preço do produto
        tk.Label(self, text='Preço do produto:').grid(row=2, column=0)
        self.preco_produto_entry = tk.Entry(self)
        self.preco_produto_entry.grid(row=2, column=1)

        # Label e Entry para a quantidade do produto
        tk.Label(self, text='Quantidade do produto:').grid(row=3, column=0)
        self.quantidade_produto_entry = tk.Entry(self)
        self.quantidade_produto_entry.grid(row=3, column=1)

        # Botão para adicionar o produto ao estoque
        self.adicionar_produto_button = tk.Button(self, text='Adicionar Produto', command=self.adicionar_produto)
        self.adicionar_produto_button.grid(row=4, column=0, columnspan=2)

        # Text widget para exibir a lista de produtos no estoque
        self.produtos_text = tk.Text(self, width=50, height=10)
        self.produtos_text.grid(row=5, column=0, columnspan=2)

    def adicionar_produto(self):
        nome = self.nome_produto_entry.get()
        tamanho = self.tamanho_produto_entry.get()
        preco = float(self.preco_produto_entry.get())
        quantidade = int(self.quantidade_produto_entry.get())

        produto = Produto(nome, tamanho, preco, quantidade)
        self.estoque.adicionar_produto(produto)

        self.atualizar_lista_produtos()

    def atualizar_lista_produtos(self):
        self.produtos_text.delete('1.0', tk.END)
        for produto in self.estoque.produtos:
            self.produtos_text.insert(tk.END, f'{produto}\n')

if __name__ == '__main__':
    app = Aplicacao()
    app.mainloop()


