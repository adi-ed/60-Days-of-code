import FreeSimpleGUI as fsg
from Zipcreator import make_archive
label1 = fsg.Text("Select files to compress: ")
input1 = fsg.Input()
choose_btn1 = fsg.FilesBrowse("Choose", key = "files")

label2 = fsg.Text("Select files to compress: ")
input2 = fsg.Input()
choose_btn2 = fsg.FolderBrowse("Choose", key = "folder")

compress_btn = fsg.Button("Compress")
output = fsg.Text(key = "output")
window = fsg.Window("File Compression", layout = [[label1,input1,choose_btn1],
                                                  [label2,input2,choose_btn2],
                                                  [compress_btn,output]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value = "Compression Completed")
    
window.read()
window.close()