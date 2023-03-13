#!/usr/local/bin/python3

import PySimpleGUI as sg
# set theme
sg.theme("DarkTeal10")
sg.set_options(	icon = "./pythonBlack.ico",
				element_padding = (8, 4),
				font = ("Sans","18"))

layout = [  [	sg.Text("This Stephen Harold Smiths User Interface\nDo you want to print shit in the terminal?!")],
          	[	sg.Button("OK",
          		bind_return_key = True,
          		mouseover_colors = ("black", "yellow"),
          		highlight_colors = ("black", "yellow"),
          		tooltip = "Print shit! in the terminal",
          		focus = True,
          		font = ("Sans", "24"),
          	 	pad = (100,(8, 4), 4)),
          	 	sg.Button("Close",
          	 	mouseover_colors = ("black", "yellow"),
          		highlight_colors = ("black", "yellow"),
          	 	tooltip  = "Exit and Close Application",
          	 	font = ("Sans", "24"),
          	 	pad = (4,(0, 4), 4))
          	]
         ]

interface = sg.Window("Stephen's UI",
						layout,
						size = (464,164),
						auto_size_text = True,
						auto_size_buttons = True,
						keep_on_top = True )

while True:
    event, values = interface.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
        
    print("shit")
    
interface.close()

