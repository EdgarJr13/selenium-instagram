from PySimpleGUI import PySimpleGUI as sg
from bot import InstagramBot as ib

# Layout
sg.theme('Reddit')

layout = [
    [sg.Text('Usuário'), sg.Input(key='username', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# Window

janela = sg.Window('Login', layout)

# Read events
while True:
    evento, valor = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'Entrar':
        run = ib('username', 'senha')
        run.login()