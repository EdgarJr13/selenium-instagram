from PySimpleGUI import PySimpleGUI as sg

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
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break