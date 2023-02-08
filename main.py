import PySimpleGUI as sg
import zipmodule


label1 = sg.Text('Select files:')
input_box1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")
label2 = sg.Text('Destination:')
input_box2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Compress", key='zip')
output_label = sg.Text("", key='output', text_color='green')

layout = [[label1, input_box1, choose_button1],
          [label2, input_box2, choose_button2],
          [compress_button, output_label]]

window = sg.Window('Zip My Files', layout=layout)

while True:
    event, values = window.read()
    print('event: ', event)
    print('values: ', values)
    filepath = values['files'].split(";")
    folder = values['folder']
    zipmodule.make_zip(filepath, folder)
    window['output'].update(value="File zip berhasil")


window.close()
