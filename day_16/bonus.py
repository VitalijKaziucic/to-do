import PySimpleGUI as sg
from zipfile import ZipFile
import os
from datetime import datetime
import shutil


def archive_files(*, folder, files):
    file_name = datetime.now()
    with ZipFile(folder + f"/{file_name}.zip", mode="w") as zip_write:

        for file in files:
            folders, file_to_zip = os.path.split(file)
            zip_write.write(file_to_zip)




layout = [
    [sg.Text(text="Select files to compress:"),
     sg.Input(size=(30, 1), key="-files-"),
     sg.FilesBrowse(button_text="Choose")],
    [sg.Text(text="Select destination folder:"),
     sg.Input(size=(30, 1), key="-folder-"),
     sg.FolderBrowse(button_text="Choose")],
    [sg.Button(button_text="Compress", key="-Compress-"),
     sg.Text(size=(40, 1), key="-zip-", text_color="green", font="Bold")]
]

window = sg.Window(title="File Zipper", layout=layout)

while 1:
    event, values = window.read()

    match event:
        case sg.WIN_CLOSED:
            break
        case "-Compress-":
            files = values["-files-"].split(";")
            folder = values["-folder-"]
            if files and folder:
                archive_files(folder=folder, files=files)
                window["-zip-"].update("Compression was completed!")
                window["-files-"].update("")
                window["-folder-"].update("")

window.close()
