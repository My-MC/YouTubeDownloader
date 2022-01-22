from yt_dlp import YoutubeDL


def webm(x):
    ydl_opts = {
        "format": "best"
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(x)


if __name__ == "__main__":
    url = input("type : ")
    webm(url)
