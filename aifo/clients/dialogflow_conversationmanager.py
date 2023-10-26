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

        
    def send_user_message(self, query):
        log = logging.getLogger("rich")
        text_input = dialogflow.TextInput(text=query, language_code=self.language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        response = self.session_client.detect_intent(
            session=self.session, query_input=query_input
        )

        current_intent = response.query_result.intent.display_name
        log.info(f"current_intent={current_intent}")
        
        parameters = response.query_result.parameters
        if parameters:
            for param, value in parameters.items():
                self.params[param] = value
        log.info(self.params)

        if current_intent == "DownloadVideoWithURL-format":
            log.info("downloading ")
            youtube_client.download(self.params["url"])
        if current_intent == "DownloadVideoWithURL-yes-cancel" or response.query_result.intent.is_fallback:
            self.reset_params()

        return response.query_result.query_text, response.query_result.fulfillment_text
    
    def reset_params(self):
        self.params = dict()