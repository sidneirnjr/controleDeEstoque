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


