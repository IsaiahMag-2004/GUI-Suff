#First step you must always do is import the framework
import PySimpleGUI as sg #sg makes it easier to type in instead of typing PySimpleGUI every time

"""
Can do this in the windopw file, but this makes easier to read|Each nested list inside this list acts as another row in the window
The first element you see in each of these save for input - which requires no parameters is the only required parameters for each of these elements
To add elements to each row you simply need to seperate them with a Comma
This is the most common / industry standard way that people crate windows
sg.Text("Text", enable_events=True, key="-TEXT-") - Example of turning a function which normally dosnt have event capability by default into a button / event  
"""
layout = [
    [sg.Text("Text", key="-TEXT-"), sg.Spin(["Item 1", "Item 2"])],
    [sg.Button("Button", key="-BUTTON1-")], 
    [sg.Input(key="-INPUT-")],
    [sg.Text("Hello"), sg.Button("Test Button", key="-BUTTON2-")]
]


#Create the window / always the starting point of your app
window = sg.Window("Title", layout) 

#Adress the issue where when you press a button the window just closes

while True:
    event, values = window.read() #.read() reads the window and waits for any kjind of event, or any kind of event value which it can return to you visually / execute assocaited functions

    if event == sg.WINDOW_CLOSED: #Used to close the window/terminate the program when the close button is pressed
        break

    if event == "-BUTTON1-":
        print(values["-INPUT-"]) #Prints to the terminal not the screen | values("-INPUT-") allows you to only display the value or use the value of the given key passed in to values as a string

    if event == "-BUTTON2-":
        window["-TEXT-"].update(values["-INPUT-"])

    
window.close 
