from yt_dlp import YoutubeDL


def best(x):
    ydl_opts = {
        "format": "bestvideo+bestaudio",
        "outtmpl": "%(title)s.%(ext)s",
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(x)


if __name__ == "__main__":
    url = input("type : ")
    best(url)
