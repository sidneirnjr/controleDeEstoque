import PySimpleGUI as sg
from src.menu import menu_cadastro, menu_consulta, menu_relatorio, menu_estoque


# Define o layout da janela principal
layout = [
    [sg.Text('Controle de Estoque', font=('Helvetica', 20), justification='center')],
    [sg.Text('Selecione uma opção:', font=('Helvetica', 14), justification='center')],
    [sg.Button('Cadastro de Produto', font=('Helvetica', 12)), sg.Button('Consulta de Produto', font=('Helvetica', 12))],
    [sg.Button('Alteração de Produto', font=('Helvetica', 12)), sg.Button('Remoção de Produto', font=('Helvetica', 12))],
    [sg.Button('Relatório de Produtos', font=('Helvetica', 12)), sg.Button('Estoque', font=('Helvetica', 12))],
    [sg.Button('Sair', font=('Helvetica', 12))]
]

# Cria a janela principal
janela = sg.Window('Controle de Estoque', layout)

# Loop principal da aplicação
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'Sair':
        break
    elif evento == 'Cadastro de Produto':
        # Chama o menu de cadastro de produto
        menu_cadastro()
    elif evento == 'Consulta de Produto':
        # Chama o menu de consulta de produto
        menu_consulta()
    elif evento == 'Alteração de Produto':
        # Chama o menu de alteração de produto
        menu_cadastro(edit=True)
    elif evento == 'Remoção de Produto':
        # Chama o menu de remoção de produto
        menu_consulta(remove=True)
    elif evento == 'Relatório de Produtos':
        # Chama o menu de relatório de produtos
        menu_relatorio()
    elif evento == 'Estoque':
        # Chama o menu de controle de estoque
        menu_estoque()

# Fecha a janela principal e encerra a aplicação
janela.close()
