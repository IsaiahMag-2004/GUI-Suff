import PySimpleGUI as sg

layout = [
    [sg.Text(" ", key="-TEXT-")],
    [sg.Button("E", key="-EQUATE-"), sg.Button("C", key="-CLEAR-")],
    [sg.Button("7", key="-NUM7-"), sg.Button("8", key="-NUM8-"), sg.Button("9", key="-NUM9-"), sg.Button("%", key="-DIVIDE-")],
    [sg.Button("4", key="-NUM4-"), sg.Button("5", key="-NUM5-"), sg.Button("6", key="-NUM6-"), sg.Button("*", key="-MULTIPLY-")],
    [sg.Button("1", key="-NUM1-"), sg.Button("2", key="-NUM2-"), sg.Button("3", key="-NUM3-"), sg.Button("-", key="-SUBTRACT-")],
    [sg.Button("0", key="-NUM0-"), sg.Button(".", key="-PERIOD-"), sg.Button("+", key="-ADD-")]

]

window = sg.Window("Calculator", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break


window.close()