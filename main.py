import PySimpleGUI as sg
import youtube_dl


def yt_dl(link):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:  # Download .mp4 from YouTube
        video = ydl.extract_info(str(link), download=True)

        name = str(ydl.prepare_filename(video))


#   GUI part
# ----------- Create the layouts this Window will display -----------
sg.theme('DarkBlack1')  # Add a touch of color
home_screen = [[sg.Text('Youtube downloader')],
               [sg.Text('Enter link of the video to download'), sg.InputText()],
               [sg.Button('Download'), sg.Button('Exit')],
               [sg.Text('by: phenriquep00')]]

download_completed = [[sg.Text('Download Completed')],
                      [sg.Button('Download other video')], [sg.Button('Exit')],
                      [sg.Text('by: phenriquep00')]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(home_screen, key='-COL1-'),
           sg.Column(download_completed, visible=False, key='-COL2-')]]

window = sg.Window('YouTube Downloader', layout)

layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event in 'ExitExit0':  # if user closes window or clicks cancel
        break
    if event == 'Download':
        window['-COL1-'].update(visible=False)
        yt_dl(values[0])
        window['-COL2-'].update(visible=True)
window.close()
