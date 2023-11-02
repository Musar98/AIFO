from google.cloud import dialogflow
from aifo.clients import youtube_client
import logging


class ConversationManager:
    def __init__(self, project_id='aifo-project1', session_id='session_id', language_code='en'):
        log = logging.getLogger("rich")
        log.info("setting up dialog flow conversation manager")
        log.info(f"project_id={project_id}")
        log.info(f"session_id={session_id}")
        log.info(f"language_code={language_code}")
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(project_id, session_id)
        self.language_code = language_code
        self.params = dict()
        self.current_response = None
        self.log = logging.getLogger("rich")

    def act_on_intent(self, intent):
        if intent == "DownloadVideoWithURL-yes-cancel":
            self.reset_params()
            return

        if intent == "DownloadVideoWithURL-format":
            if self.params['format'] is ['audio']:
                self.log.info("starting audio download")
                youtube_client.download(self.params["url"])
            else:
                self.log.info("starting video download")
                youtube_client.download(self.params["url"], True)

    def store_parameters(self, response_arguments):
        if response_arguments:
            for param, value in response_arguments.items():
                self.params[param] = value

    # returns result query text, fullfillment text and current intent 
    def send_user_message(self, query):
        text_input = dialogflow.TextInput(text=query, language_code=self.language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        response = self.session_client.detect_intent(
            session=self.session, query_input=query_input
        )
        self.current_response = response
        self.store_parameters(response.query_result.parameters)

        return response.query_result.fulfillment_text, response.query_result.intent.display_name

    def reset_params(self):
        self.params = dict()
