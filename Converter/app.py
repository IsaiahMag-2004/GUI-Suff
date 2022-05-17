import PySimpleGUI as sg
#Create general lay out for the program and inser the elements we need
layout = [
    [sg.Input(key="-INPUT-"), sg.Spin(["km to mile", "kg to pounds"], key="-SPINNER-"), sg.Button("Convert", key="-CONVERTER_BUTTON-")],
    [sg.Text("Output: "), sg.Text("base", key="-OUTPUT-")],
]

#Create the window
window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    #Close Terminate program when exit button is pressed
    if event == sg.WINDOW_CLOSED:
        break

    #Conversion
    if event == "-CONVERTER_BUTTON-":
        #Collect the values
        user_input = float(values["-INPUT-"])
        conversion_choice = values["-SPINNER-"]

        
        #convert
        if conversion_choice == "km to mile":
            # window["-OUTPUT-"].update(user_input * 0.62137)
            window["-OUTPUT-"].update(user_input * 0.62137)
        else:
            # window["-OUTPUT-"].update(user_input * 2.20462)
            window["-OUTPUT-"].update(user_input * 2.20462)

window.close