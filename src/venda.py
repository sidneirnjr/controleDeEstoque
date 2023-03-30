class Venda:
    def __init__(self, data):
        self.data = data
        self.produtos = []
        self.valor_total = 0

    def adicionar_produto(self, produto, quantidade):
        if produto.get_quantidade() < quantidade:
            print("Quantidade em estoque insuficiente.")
            return
        produto.set_quantidade(produto.get_quantidade() - quantidade)
        self.produtos.append((produto, quantidade))
        self.valor_total += produto.get_preco_venda() * quantidade

    def imprimir(self):
        print("Data: ", self.data)
        print("Produtos: ")
        for produto, quantidade in self.produtos:
            print(produto.get_nome(), " - ", quantidade, " - R$", produto.get_preco_venda() * quantidade)
        print("Valor total: R$", self.valor_total)


class VendaInterface:
    def __init__(self, master):
        self.master = master
        master.title("Controle de Estoque - Venda")

        # criar widgets
        self.lbl_codigo = Label(master, text="Código:")
        self.ent_codigo = Entry(master)

        self.lbl_nome = Label(master, text="Nome:")
        self.ent_nome = Entry(master)

        self.lbl_preco = Label(master, text="Preço:")
        self.ent_preco = Entry(master)

        self.lbl_quantidade = Label(master, text="Quantidade:")
        self.ent_quantidade = Entry(master)

        self.lbl_valor_total = Label(master, text="Valor Total:")
        self.ent_valor_total = Entry(master, state="readonly")

        self.btn_calcular = Button(master, text="Calcular", command=self.calcular_valor_total)
        self.btn_vender = Button(master, text="Vender", command=self.vender_produto)

        # posicionar widgets
        self.lbl_codigo.grid(row=0, column=0, padx=5, pady=5)
        self.ent_codigo.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_nome.grid(row=1, column=0, padx=5, pady=5)
        self.ent_nome.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_preco.grid(row=2, column=0, padx=5, pady=5)
        self.ent_preco.grid(row=2, column=1, padx=5, pady=5)

        self.lbl_quantidade.grid(row=3, column=0, padx=5, pady=5)
        self.ent_quantidade.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_valor_total.grid(row=4, column=0, padx=5, pady=5)
        self.ent_valor_total.grid(row=4, column=1, padx=5, pady=5)

        self.btn_calcular.grid(row=5, column=0, padx=5, pady=5)
        self.btn_vender.grid(row=5, column=1, padx=5, pady=5)

    def calcular_valor_total(self):
        quantidade = self.ent_quantidade.get()
        preco = self.ent_preco.get()

        if quantidade and preco:
            valor_total = float(quantidade) * float(preco)
            self.ent_valor_total.config(state="normal")
            self.ent_valor_total.delete(0, END)
            self.ent_valor_total.insert(0, valor_total)
            self.ent_valor_total.config(state="readonly")
        else:
            messagebox.showerror("Erro", "Preencha os campos de quantidade e preço")

    def vender_produto(self):
        codigo = self.ent_codigo.get()
        nome = self.ent_nome.get()
        quantidade = self.ent_quantidade.get()
        preco = self.ent_preco.get()

        if codigo and nome and quantidade and preco:
            quantidade = int(quantidade)
            preco = float(preco)

            produto = Produto(codigo, nome, preco, quantidade)

            try:
                venda = Venda(produto, quantidade)
                venda.efetuar_venda()
                messagebox.showinfo("Sucesso", "Venda realizada com sucesso")
            except EstoqueException as e:
                messagebox.showerror("Erro", e)
        else:
            messagebox.showerror("Erro", "Preencha todos os campos")
