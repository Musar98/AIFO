import logging

from pytube import YouTube

class YoutubeDownloadManager:
    def __init__(self, logger=logging.getLogger("rich")):
        self.log = logger

    def download(self, url, video=True):
        self.log.info(f"Attemting to download {url}")
        yt = YouTube(url)

        if video:
            yt.streams.get_highest_resolution().download()
        else:
            yt.streams.get_audio_only().download()