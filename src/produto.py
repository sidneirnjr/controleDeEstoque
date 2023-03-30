from tkinter import *
from tkinter import messagebox


class Produto:
    def __init__(self, codigo, nome, descricao, preco_custo, preco_venda, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.quantidade = quantidade

    def calcular_lucro(self):
        return self.preco_venda - self.preco_custo

    def imprimir(self):
        print("Código: ", self.codigo)
        print("Nome: ", self.nome)
        print("Descrição: ", self.descricao)
        print("Preço de custo: ", self.preco_custo)
        print("Preço de venda: ", self.preco_venda)
        print("Quantidade em estoque: ", self.quantidade)

    @staticmethod
    def pesquisar_por_codigo(produtos, codigo):
        for produto in produtos:
            if produto.get_codigo() == codigo:
                return produto
        return None

    @staticmethod
    def pesquisar_por_palavra_chave(produtos, palavra_chave):
        resultados = []
        for produto in produtos:
            if palavra_chave in produto.get_nome() or palavra_chave in produto.get_descricao():
                resultados.append(produto)
        return resultados


class ProdutoInterface:
    def __init__(self, master):
        self.master = master
        master.title("Controle de Estoque - Produto")

        # Criação dos widgets
        self.label_id = Label(master, text="ID:")
        self.label_nome = Label(master, text="Nome:")
        self.label_valor = Label(master, text="Valor:")
        self.label_unidade = Label(master, text="Unidade:")

        self.entry_id = Entry(master)
        self.entry_nome = Entry(master)
        self.entry_valor = Entry(master)
        self.entry_unidade = Entry(master)

        self.button_adicionar = Button(master, text="Adicionar", command=self.adicionar_produto)
        self.button_remover = Button(master, text="Remover", command=self.remover_produto)
        self.button_visualizar = Button(master, text="Visualizar", command=self.visualizar_produtos)

        # Layout dos widgets na janela
        self.label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)
        self.label_nome.grid(row=1, column=0)
        self.entry_nome.grid(row=1, column=1)
        self.label_valor.grid(row=2, column=0)
        self.entry_valor.grid(row=2, column=1)
        self.label_unidade.grid(row=3, column=0)
        self.entry_unidade.grid(row=3, column=1)

        self.button_adicionar.grid(row=4, column=0)
        self.button_remover.grid(row=4, column=1)
        self.button_visualizar.grid(row=5, column=0, columnspan=2)

        # Criação do objeto Produto
        self.produto = Produto()

    def adicionar_produto(self):
        id = self.entry_id.get()
        nome = self.entry_nome.get()
        valor = self.entry_valor.get()
        unidade = self.entry_unidade.get()

        if self.produto.adicionar_produto(id, nome, valor, unidade):
            messagebox.showinfo("Produto", f"Produto '{nome}' adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Não foi possível adicionar o produto.")

        self.entry_id.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_valor.delete(0, END)
        self.entry_unidade.delete(0, END)

    def remover_produto(self):
        id = self.entry_id.get()

        if self.produto.remover_produto(id):
            messagebox.showinfo("Produto", f"Produto com ID '{id}' removido com sucesso!")
        else:
            messagebox.showwarning("Atenção", f"Não foi possível remover o produto com ID '{id}'.")

        self.entry_id.delete(0, END)

    def visualizar_produtos(self):
        produtos = self.produto.listar_produtos()

        if produtos:
            messagebox.showinfo("Produtos", produtos)
        else:
            messagebox.showerror("Erro", "Não foi possível obter os produtos.")


if __name__ == '__main__':
    root = Tk()
    app = ProdutoInterface(root)
    root.mainloop()

