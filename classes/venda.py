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
