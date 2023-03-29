class Relatorio:
    def __init__(self, vendas: List[Venda]):
        self.vendas = vendas

    def produtos_mais_vendidos(self, n: int) -> List[Tuple[str, int]]:
        """
        Retorna uma lista com os n produtos mais vendidos.
        """
        produtos_vendidos = {}
        for venda in self.vendas:
            for produto_vendido in venda.produtos:
                nome = produto_vendido.produto.nome
                if nome in produtos_vendidos:
                    produtos_vendidos[nome] += produto_vendido.quantidade
                else:
                    produtos_vendidos[nome] = produto_vendido.quantidade

        return sorted(produtos_vendidos.items(), key=lambda x: x[1], reverse=True)[:n]

    def vendas_por_periodo(self, data_inicial: date, data_final: date) -> List[Venda]:
        """
        Retorna uma lista com as vendas realizadas no período especificado.
        """
        vendas_periodo = []
        for venda in self.vendas:
            if data_inicial <= venda.data <= data_final:
                vendas_periodo.append(venda)

        return vendas_periodo
