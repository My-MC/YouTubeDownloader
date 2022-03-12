from yt_dlp import YoutubeDL


def webm(self):
    ydl_opts = {"format": "best"}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(self)


if __name__ == "__main__":
    url = input("type : ")
    webm(url)
