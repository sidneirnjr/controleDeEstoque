from tkinter import *
from tkinter import messagebox
from .estoque import Estoque, EstoqueInterface


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, codigo):
        produto = self.pesquisar_por_palavra_chave(codigo)
        if produto is not None:
            self.produtos.remove(produto)
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado.")

    def alterar_quantidade(self, codigo, quantidade):
        produto = self.pesquisar_por_palavra_chave(codigo)
        if produto is not None:
            produto.set_quantidade(quantidade)
            print("Quantidade alterada com sucesso!")
        else:
            print("Produto não encontrado.")

    def listar_produtos(self):
        for produto in self.produtos:
            produto.imprimir()

    def pesquisar_por_palavra_chave(self, palavra_chave):
        for produto in self.produtos:
            if palavra_chave.lower() in produto.get_nome().lower() or palavra_chave.lower() in produto.get_descricao().lower():
                return produto
        return None


class EstoqueInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Controle de Estoque")
        self.master.geometry("600x400")

        self.estoque = Estoque()

        self.lbl_title = Label(self.master, text="Controle de Estoque", font=("Arial", 18))
        self.lbl_title.pack(pady=10)

        self.frame = Frame(self.master)
        self.frame.pack(pady=20)

        self.lbl_id = Label(self.frame, text="ID do Produto:")
        self.lbl_id.grid(row=0, column=0, padx=10)

        self.entry_id = Entry(self.frame, width=30)
        self.entry_id.grid(row=0, column=1)

        self.lbl_quantidade = Label(self.frame, text="Quantidade:")
        self.lbl_quantidade.grid(row=1, column=0, padx=10)

        self.entry_quantidade = Entry(self.frame, width=30)
        self.entry_quantidade.grid(row=1, column=1)

        self.btn_add = Button(self.frame, text="Adicionar ao Estoque", command=self.adicionar_estoque)
        self.btn_add.grid(row=2, column=0, columnspan=2, pady=10)

        self.btn_remover = Button(self.frame, text="Remover do Estoque", command=self.remover_estoque)
        self.btn_remover.grid(row=3, column=0, columnspan=2, pady=10)

        self.btn_visualizar = Button(self.frame, text="Visualizar Estoque", command=self.visualizar_estoque)
        self.btn_visualizar.grid(row=4, column=0, columnspan=2, pady=10)

    def adicionar_estoque(self):
        id_produto = self.entry_id.get()
        quantidade = self.entry_quantidade.get()

        if not id_produto or not quantidade:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")
            return

        if quantidade <= 0:
            messagebox.showerror("Erro", "A quantidade deve ser maior que zero.")
            return

        produto = self.estoque.adicionar_estoque(id_produto, quantidade)

        if produto:
            messagebox.showinfo("Sucesso", f"Produto '{produto.nome}' adicionado ao estoque.")
        else:
            messagebox.showerror("Erro", f"Não foi possível adicionar o produto ao estoque.")

        self.entry_id.delete(0, END)
        self.entry_quantidade.delete(0, END)

    def remover_estoque(self):
        id_produto = self.entry_id.get()
        quantidade = self.entry_quantidade.get()

        if not id_produto or not quantidade:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")
            return

        if quantidade <= 0:
            messagebox.showerror("Erro", "A quantidade deve ser maior que zero.")
            return

        produto = self.estoque.remover_estoque(id_produto, quantidade)

        if produto:
            messagebox.showinfo("Sucesso", f"Produto '{produto.nome}' removido")

            if produto.estoque < 0:
                messagebox.showwarning("Atenção",
                                       f"A quantidade do produto '{produto.nome}' no estoque ficou negativa.")

            else:
                messagebox.showerror("Erro", f"Não foi possível remover o produto do estoque.")

            self.entry_id.delete(0, END)
            self.entry_quantidade.delete(0, END)

    def visualizar_estoque(self):
        estoque = self.estoque.listar_estoque()

        if estoque:
            messagebox.showinfo("Estoque", estoque)
        else:
            messagebox.showerror("Erro", "Não foi possível obter o estoque.")

    if __name__ == '__main__':
        root = Tk()
        app = EstoqueInterface(root)
        root.mainloop()



