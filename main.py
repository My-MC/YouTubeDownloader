import PySimpleGUI as Sg
import base64
import ctypes
import downloader.wav as wav
import downloader.mp3 as mp3
import downloader.webm as webm
import downloader.best as best


def main():
    Sg.theme("default1")

    combo_val = ["best", "標準", "mp3", "wav"]

    myappid = "my_mc.youtubedownloader.1_0"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    icon = base64.b64encode(open(r"icon.png", "rb").read())

    title = "Youtube Downloader"
    layout = [
        [Sg.Text("URL : "), Sg.InputText(key="-URL-")],
        [Sg.Combo(combo_val, default_value="選択してください", size=(20, 1), key="-TYPE-")],
        [Sg.Button("Download", key="-ENTER-")],
        [Sg.Text(key="-RESULT-", size=(20, 1))],
        [Sg.Output(size=(50, 10))],
    ]
    window = Sg.Window(title, layout, size=(400, 300), icon=icon, finalize=True)

    while True:
        event, values = window.read()
        if event == "-ENTER-":
            window["-RESULT-"].update("Now downloading")
            print(values["-URL-"])
            url = values["-URL-"]
            finish_msg = "Download was finished"
            if values["-TYPE-"] == "wav":
                wav.wav(url)
                window["-RESULT-"].update(finish_msg)
            elif values["-TYPE-"] == "mp3":
                mp3.mp3(url)
                window["-RESULT-"].update(finish_msg)
            elif values["-TYPE-"] == "標準":
                webm.webm(url)
                window["-RESULT-"].update(finish_msg)
            elif values["-TYPE-"] == "best":
                best.best(url)
                window["-RESULT-"].update(finish_msg)

        if event == Sg.WINDOW_CLOSED:
            break


if __name__ == "__main__":
    main()
