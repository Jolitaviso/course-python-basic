import PySimpleGUI as sg

layout = [
    [sg.Text("Koks tavo vardas?", font="Verdana 15")],
    [sg.Input(key="-NAME-", font="Terminal 15")],
    [
        sg.Button("Pasisveikinti", key="-HELLO-"), 
        sg.Button("Atsisveikinti", key="-BYE-"),
    ],
    [sg.Text(size=(40, 1), key="-OUTPUT-", font="Verdana 15")],
]

window = sg.Window("LABAS", layout)
sg.DEFAULT_FONT

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "-HELLO-":
        window["-OUTPUT-"].update(
            f"Sveiki {values['-NAME-']}",
            text_color="#99ff99"
        )
    elif event == "-BYE-":
        window["-OUTPUT-"].update(
            f"Viso gero {values['-NAME-']}",
            text_color="#ff9999"
        )

window.close()


from PIL import Image
import PySimpleGUI as sg
import io

image = Image.open('PTU20_live/ai_guy.webp')
with io.BytesIO() as bio:
    image.save('PTU20_live/ai_guy.png', format="PNG")
    image_data = bio.getvalue()

layout = [
    # [sg.Image(filename='PTU20_live/ai_guy.png', size=image.size)], #, expand_x=True, expand_y=True
    [sg.Button(image_source='PTU20_live/ai_guy.png')],
]

window = sg.Window("AI GUY", layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
