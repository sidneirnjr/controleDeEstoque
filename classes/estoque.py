class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def pesquisar(self, chave):
        resultados = []
        for produto in self.produtos:
            if chave.lower() in produto.get_codigo().lower() or chave.lower() in produto.get_nome().lower():
                resultados.append(produto)
        return resultados
