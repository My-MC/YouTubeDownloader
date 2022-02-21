import PySimpleGUI as Sg
import downloader.wav as wav
import downloader.mp3 as mp3
import downloader.webm as webm
import downloader.best as best

Sg.theme("default1")

combo_val = ["best", "標準", "mp3", "wav"]

icon = b"iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABhmlDQ1BJQ0MgcHJvZmlsZQAAKM" \
       b"+VkT1Iw1AUhU9TiyIVBwuKOGSoLloQFXWUKBbBQmkrtOpg8tI/aNKQpLg4Cq4FB38Wqw4uzro6uAqC4A" \
       b"+Io5OToouUeF9SaBEqeOHxPs5753DffYBQKzHN6hgHNN02E1FJTGdWxc5X+NCPAGYwKjPLiCUXU2hbX/d0m+ouwrPwv" \
       b"+pRsxYDfCLxHDNMm3iDeHrTNjjvE4dYQVaJz4nHTGqQ+JHrisdvnPMuCzwzZKYS88QhYjHfwkoLs4KpEU8Rh1VNp3wh7bHKeYuzVqqwRp" \
       b"/8hcGsvpLkOq0hRLGEGOIQoaCCIkqwEaFdJ8VCgs6lNv5B1x8nl0KuIhg5FlCGBtn1g//B79lauckJLykoAYEXx/kYBjp3gXrVcb6PHad" \
       b"+AvifgSu96S/XgNlP0qtNLXwE9G4DF9dNTdkDLneAgSdDNmVX8tMScjng/Yy+KQP03QLda97cGuc4fQBSNKvlG+DgEBjJU" \
       b"/Z6m3d3tc7tzzvu/CD9AMxVcsufQt72AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAABmJLR0QA" \
       b"/wAAAAAzJ3zzAAAAB3RJTUUH5gEXBTsaO3zAAAAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAGdSURBVDhPnVI7TwJBGJy78zgVH0dICMZETIi9iT0NtRT8AisbS0saKC2NDYmtPTT0RmgsjI0tUSTGBBWwIaB3rLPrgnqKr0nm8u238z1vDUEgiGIRKJWAeh14fgZWV4F0GsjlAMvSIg2ZYIz9fZnte25va/Er6NHIZj+LJ3FpSQfxqL6/qRzk5qYKpSW/r85byxKXtj0+P5qmOFpYUHab9sg/ZrMprHw8nkelovaxF41ifTBA0XWxOBzingvzDQNP5GEkgpupKZw7DuKehzmZotOBqbatsdHvI8zAK9tGdWZGBUic0q7T12bC49lZGMpLlMvsI5lU7VyEQh/al+wG2u4b/OvvzpKGSCQEGg1VkQlU22e01zjKA+2DVgu7sRgsynscJeb7iJI73a5qwhCplMDJCa7ZrqzfYdA8x4hQdEefnN+nsGeamOZ9iHfL3EFY1uc+IAoF1cq/mMlwBM8T0Mv6M2o1mYaQzzOY/SeurKhQWhryeX4lnESNN0tCPs+vxO+pK49ATwB8nmJrSwjXfQtyHLUwUa1q0QhCvADCFvApF20t8QAAAABJRU5ErkJggg== "

title = "Youtube Downloader"
layout = [
    [Sg.Text("URL : "), Sg.InputText(key="-URL-")],
    [Sg.Combo(combo_val, default_value="選択してください", size=(20, 1), key="-TYPE-")],
    [Sg.Button("Download", key="-ENTER-")],
    [Sg.Text(key="-RESULT-", size=(20, 1))],
    [Sg.Output(size=(50, 10))],
]
window = Sg.Window(title, layout, size=(400, 300), icon= icon)

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
        if values["-TYPE-"] == "mp3":
            mp3.mp3(url)
            window["-RESULT-"].update(finish_msg)
        if values["-TYPE-"] == "標準":
            webm.webm(url)
            window["-RESULT-"].update(finish_msg)
        if values["-TYPE-"] == "best":
            best.best(url)
            window["-RESULT-"].update(finish_msg)

    if event == Sg.WINDOW_CLOSED:
        break
