# Create an algorithm that generates a random value. 
# The player must try to guess the generated number.

import PySimpleGUI as sg
import random

sg.theme('black')

def guess_the_number(num_min, num_max):
    secret_number = random.randint(num_min, num_max)
    attempts = 0
    layout = [

        [sg.Text(f'Try to guess the number between {num_min} e {num_max}')],
        [sg.Input(key='-GUESS-')],
        [sg.Button('Send'), sg.Button('Quit')],
        [sg.Text('', key='-RESULT-')],
    ]
    window = sg.Window('Guess the number', layout)
    while True:
        event,values=window.read()

        if event in (sg.WIN_CLOSED, 'Quit'):
            break

        guess = int(values['-GUESS-'])

        if guess == secret_number:
            attempts+=1
            window['-RESULT-'].update(f'Congratulations, you got the number {secret_number} em {attempts} tries.')

        elif guess < secret_number:
            attempts+=1
            window['-RESULT-'].update(f'Try a larger number.')

        else:
            attempts+=1
            window['-RESULT-'].update(f'Try a smaller number.')
    window.close()

layout = [
    [sg.Text('')],
    [sg.Text('*** GUESS THE NUMBER ***',justification='center',background_color='white',text_color='black')],
    [sg.Text('')],
    [sg.Image(r'C:\Users\sandro.oliveira\Desktop\Chute_o_numero\chute.png')],
    [sg.Text('Type the minimum value of the range: '),sg.Input(key='-MIN-',size=(5,1))],
    [sg.Text('Type the maximum value of the range:'),sg.Input(key='-MAX-',size=(5,1))],
    [sg.Button('Start the game'), sg.Button('Quit')],
]
window = sg.Window('Guess the number', layout, element_justification='c')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Quit'):
        break

    num_min=int(values['-MIN-'])
    num_max=int(values['-MAX-'])
    
    window.hide()
    guess_the_number(num_min, num_max)
    window.un_hide()
    
window.close()
