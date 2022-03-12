from yt_dlp import YoutubeDL


def mp3(self):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {"key": "FFmpegMetadata"},
        ],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(self)


if __name__ == "__main__":
    url = input("type")
    mp3(url)
