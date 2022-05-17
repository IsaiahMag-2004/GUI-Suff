import PySimpleGUI as sg

"""Creating list in Python is like creating a big table"""
layout = [
    [sg.Text('Text', enable_events=True, key="-TEXT-"), sg.Spin(["Item 1", "Item 2"])],
    [sg.Button('Button', key="-BUTTON1-")],
    [sg.Input(key="-INPUT-")], #This Key will allow you to specify which input element you are allowing data to come from
    [sg.Text("Challange 1"), sg.Button("Button", key="-BUTTON2-")]
] #Each list is its own row in the window
#Key gives us a more general way to find and identify buttons/elements and is used most often becuase near every element has the key parameter 
#A convention with elements / keys is the name in all caps followed and precended by a dash -BUTTON1-
root = sg.Window(title="Converter", layout=layout)

while True: #At just this stage you can't close the window
    event, values = root.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '-BUTTON1-':
        print(values["-INPUT-"]) #Prints to the terminal | In its current state prints the inputed value
    if event == "-BUTTON2-":
        root["-TEXT-"].update(values["-INPUT-"]) #Changes the value of the first text secton we have on row one to the inputed value 
    if event == "-TEXT-": #Every element in this framework can be given an event effectivly tunring them into a button
        print("Text was pressed")

root.close() #Ensures that the window is closed



