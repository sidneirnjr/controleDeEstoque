import tkinter as tk
from tkinter import ttk

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


class RelatorioInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Relatório")

        # Criação do frame
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Label do título
        titulo_label = ttk.Label(main_frame, text="Relatório")
        titulo_label.pack(pady=10)

        # Label para selecionar o período do relatório
        periodo_label = ttk.Label(main_frame, text="Selecione o período do relatório:")
        periodo_label.pack(pady=10)

        # Criação do combobox para selecionar o período
        periodo_combobox = ttk.Combobox(main_frame, values=["Diário", "Semanal", "Mensal"])
        periodo_combobox.pack()

        # Botão para gerar o relatório
        gerar_relatorio_button = ttk.Button(main_frame, text="Gerar Relatório")
        gerar_relatorio_button.pack(pady=20)

        # Botão para fechar a janela
        fechar_button = ttk.Button(main_frame, text="Fechar", command=self.root.destroy)
        fechar_button.pack(pady=10)
