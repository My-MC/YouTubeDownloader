from main import main
import yaml
import ctypes
import base64
import urllib.request
import shutil
import os
from distutils.dir_util import copy_tree
import PySimpleGUI as Sg

with open("conf/conf.yml", "r") as f:
    x = yaml.safe_load(f)
    if x["installed"] == None:
        Sg.theme("default1")

        myappid = "my_mc.youtubedownloader.1_0"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        icon = base64.b64encode(open(r"icon.png", "rb").read())

        title = "Youtube Downloader Setup"
        layout = [
            [Sg.Text("Do you have FFmpeg installed?")],
            [Sg.Text("FFmpegはインストールされていますか？")],
            [Sg.Button("Yes", key="-Yes-"), Sg.Button("No, I don't know", key="-No-")],
            [Sg.Button("Finish", key="-Finish-")],
            [Sg.Text(key="-RESULT-")],
            [Sg.Output(size=(50, 10))],
        ]
        window = Sg.Window(title, layout, size=(400, 300), icon=icon, finalize=True)

        while True:
            event, values = window.read()

            def installed():
                with open("conf/conf.yml", "w") as w:
                    yw = {"installed": "true"}
                    yaml.dump(yw, w, encoding="utf-8", allow_unicode=True)

            if event == "-Yes-":
                window["-Yes-"].update(" ")
                installed()
                window["-RESULT-"].update(
                    "Finished setting up. Please press Finish button"
                )

            elif event == "-No-":
                window["-RESULT-"].update("Now setting up")
                window["-Yes-"].update(" ")
                window["-No-"].update(" ")
                url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n5.0-latest-win64-lgpl-5.0.zip"
                save_name = "FFmpeg.zip"
                os.mkdir("cache")
                urllib.request.urlretrieve(url, save_name)
                shutil.unpack_archive(save_name, "cache")
                copy_tree("./cache/ffmpeg-n5.0-latest-win64-lgpl-5.0/bin", "./")
                shutil.rmtree("./cache")
                os.remove(save_name)

                window["-RESULT-"].update(
                    "Finished setting up. Please press Finish button"
                )
                installed()

            elif event == "-Finish-":
                break

            if event == Sg.WINDOW_CLOSED:
                break
    if x["installed"] == "true":
        main()
