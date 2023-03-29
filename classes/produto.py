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

