from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTableWidget, QTableWidgetItem, QHeaderView, \
    QAbstractItemView, QInputDialog, QMessageBox
from PyQt5.QtGui import QIcon
from estoque import Estoque


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.setWindowTitle("Controle de Estoque")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("icon.png"))

        # Cria uma instância do estoque
        self.estoque = Estoque()

        # Cria a barra de menu
        menu_bar = self.menuBar()

        # Cria o menu "Arquivo"
        file_menu = menu_bar.addMenu("Arquivo")

        # Cria a ação "Novo"
        novo_action = QAction("Novo", self)
        novo_action.setShortcut("Ctrl+N")
        novo_action.triggered.connect(self.novo)
        file_menu.addAction(novo_action)

        # Cria a ação "Abrir"
        abrir_action = QAction("Abrir", self)
        abrir_action.setShortcut("Ctrl+O")
        abrir_action.triggered.connect(self.abrir)
        file_menu.addAction(abrir_action)

        # Cria a ação "Salvar"
        salvar_action = QAction("Salvar", self)
        salvar_action.setShortcut("Ctrl+S")
        salvar_action.triggered.connect(self.salvar)
        file_menu.addAction(salvar_action)

        # Cria a ação "Sair"
        sair_action = QAction("Sair", self)
        sair_action.setShortcut("Ctrl+Q")
        sair_action.triggered.connect(self.close)
        file_menu.addAction(sair_action)

        # Cria o menu "Editar"
        edit_menu = menu_bar.addMenu("Editar")

        # Cria a ação "Adicionar"
        adicionar_action = QAction("Adicionar", self)
        adicionar_action.setShortcut("Ctrl+A")
        adicionar_action.triggered.connect(self.adicionar)
        edit_menu.addAction(adicionar_action)

        # Cria a ação "Editar"
        editar_action = QAction("Editar", self)
        editar_action.setShortcut("Ctrl+E")
        editar_action.triggered.connect(self.editar)
        edit_menu.addAction(editar_action)

        # Cria a ação "Remover"
        remover_action = QAction("Remover", self)
        remover_action.setShortcut("Ctrl+R")
        remover_action.triggered.connect(self.remover)
        edit_menu.addAction(remover_action)

        # Cria a tabela de estoque
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(10, 10, 780, 580)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Produto", "Quantidade", "Preço"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Preenche a tabela com os dados do estoque
        self.atualizar_tabela()

    def atualizar_tabela(self):
        # Limpa a tabela
        self.table_widget.setRowCount(0)

        # Adiciona os dados do estoque à tabela
        for produto in self.estoque.listar_produtos():
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(produto["nome"]))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(produto["quantidade"])))
            self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(produto["preco"])))

        def novo(self):
            # Cria um novo estoque
            self.estoque = Estoque()

            # Atualiza a tabela
            self.atualizar_tabela()

        def abrir(self):
            # Pergunta o nome do arquivo
            nome_arquivo, ok = QInputDialog.getText(self, "Abrir arquivo", "Digite o nome do arquivo:")

            if ok and nome_arquivo:
                # Tenta abrir o arquivo
                try:
                    self.estoque.carregar(nome_arquivo)
                    self.atualizar_tabela()
                except FileNotFoundError:
                    QMessageBox.warning(self, "Erro", "Arquivo não encontrado!")

        def salvar(self):
            # Pergunta o nome do arquivo
            nome_arquivo, ok = QInputDialog.getText(self, "Salvar arquivo", "Digite o nome do arquivo:")

            if ok and nome_arquivo:
                # Tenta salvar o arquivo
                try:
                    self.estoque.salvar(nome_arquivo)
                except:
                    QMessageBox.warning(self, "Erro", "Não foi possível salvar o arquivo!")

        def adicionar(self):
            # Pergunta o nome, a quantidade e o preço do produto
            nome, ok = QInputDialog.getText(self, "Adicionar produto", "Digite o nome do produto:")
            if ok and nome:
                quantidade, ok = QInputDialog.getInt(self, "Adicionar produto", "Digite a quantidade:")
                if ok:
                    preco, ok = QInputDialog.getDouble(self, "Adicionar produto", "Digite o preço:")
                    if ok:
                        # Adiciona o produto ao estoque
                        self.estoque.adicionar_produto(nome, quantidade, preco)

                        # Atualiza a tabela
                        self.atualizar_tabela()

        def editar(self):
            # Pergunta qual produto deve ser editado
            index = self.table_widget.currentIndex()
            if index.isValid():
                row = index.row()
                nome_produto = self.table_widget.item(row, 0).text()

                # Pergunta a nova quantidade e o novo preço
                quantidade, ok = QInputDialog.getInt(self, "Editar produto", "Digite a quantidade:",
                                                     self.estoque.obter_quantidade(nome_produto))
                if ok:
                    preco, ok = QInputDialog.getDouble(self, "Editar produto", "Digite o preço:",
                                                       self.estoque.obter_preco(nome_produto))
                    if ok:
                        # Edita o produto no estoque
                        self.estoque.editar_produto(nome_produto, quantidade, preco)

                        # Atualiza a tabela
                        self.atualizar_tabela()

        def remover(self):
            # Pergunta qual produto deve ser removido
            index = self.table_widget.currentIndex()
            if index.isValid():
                row = index.row()
                nome_produto = self.table_widget.item(row, 0).text()

                # Remove o produto do estoque
                self.estoque.remover_produto(nome_produto)

                # Atualiza a tabela
                self.atualizar_tabela()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
