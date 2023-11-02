from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import logging


# https://pytube.io/en/latest/


def on_progress(stream, chunks, bytes_remaining):
    return


def on_completion():
    return


def download(link, video=False):
    log = logging.getLogger("rich")
    log.info(f"Attemting to download {link}")
    try:
        yt = YouTube(
            link,
            on_progress_callback=on_progress,
            use_oauth=False,
            allow_oauth_cache=False
        )
        log.debug("video information")
        log.debug(f"title={yt.title}")
        log.debug(f"description={yt.description}")
        log.debug(f"views={yt.views}")
        log.debug(f"publish_date={yt.publish_date}")
        log.debug(f"keywords={yt.keywords}")
        log.debug(f"age_restricted={yt.age_restricted}")
    except VideoUnavailable as e:
        log.error("the video is unavailable")
        log.exception(e)
    else:
        log.info("downloading video")
        if video:
            yt.streams.get_highest_resolution().download()
        else:
            yt.streams.get_audio_only().download()
