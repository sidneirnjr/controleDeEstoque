from estoque import Estoque
from produto import Produto
from relatorio import Relatorio
from venda import Venda


class MenuPrincipal:
    def __init__(self):
        self.estoque = Estoque()
        self.produto = Produto()
        self.relatorio = Relatorio()
        self.venda = Venda()

    def exibir_menu_principal(self):
        # Aqui você pode implementar o código para exibir o menu principal
        # e permitir que o usuário escolha as opções para acessar as funcionalidades da aplicação
        opcao = input(
            "Escolha uma opção:\n1 - Adicionar um novo produto\n2 - Remover um produto\n3 - Atualizar as informações de um produto\n4 - Pesquisar um produto pelo nome\n5 - Exibir a lista de todos os produtos no estoque\n6 - Gerar um relatório sobre o estoque\n7 - Realizar uma venda\n")

        if opcao == "1":
            self.estoque.adicionar_produto()
        elif opcao == "2":
            self.estoque.remover_produto()
        elif opcao == "3":
            self.estoque.atualizar_produto()
        elif opcao == "4":
            self.estoque.pesquisar_produto()
        elif opcao == "5":
            self.estoque.listar_produtos()
        elif opcao == "6":
            self.relatorio.gerar_relatorio()
        elif opcao == "7":
            self.venda.registrar_venda()
        else:
            print("Opção inválida. Tente novamente.")


