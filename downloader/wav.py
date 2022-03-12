from yt_dlp import YoutubeDL


def wav(self):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            },
            {"key": "FFmpegMetadata"},
        ],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(self)


if __name__ == "__main__":
    url = input("type")
    wav(url)
