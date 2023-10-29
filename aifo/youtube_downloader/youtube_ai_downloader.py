import logging
from aifo.youtube_downloader.df_conversation_manager import DfConversationManager
from aifo.youtube_downloader.youtube_download_manager import YoutubeDownloadManager

class YoutubeAIDownloader:
    
    def __init__(self, logger=logging.getLogger("rich")):
        self.log = logger
        self.diag_conv_manager = DfConversationManager()
        self.yt_download_manager = YoutubeDownloadManager()
        self.diag_params = dict()

    def run(self):
        print("Welcome, enter message")
        while True:
            user_input = input()

            try:
                response = self.diag_conv_manager.send_user_message()
            except Exception as e:
                self.output("could not interact with dialog flow")
                return
            

    def act(self, response):
        intent = response.
        if intent == "DownloadVideoWithURL-yes-cancel" or intent.is_fallback:
            self.reset_params()
            return

        if intent == "DownloadVideoWithURL-format":
            if self.params['format'] is ['audio']:
                self.log.info("starting audio download")
                youtube_client.download(self.params["url"])
            else:
                self.log.info("starting video download")
                youtube_client.download(self.params["url"], True)
        return

    def output(self, msg):
        print(msg)

    
    

    