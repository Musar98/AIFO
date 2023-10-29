import logging
from enum import Enum
from google.cloud import dialogflow

class DFConversationParametersAction(Enum):
    DOWNLOAD_AUDIO = 1
    DOWNLOAD_VIDEO = 2
    FALLBACK = 3

class DFConversationParameters:
    def __init__(self, url="", format=DFConversationParametersAction.DOWNLOAD_VIDEO):
        self.url = url
        self.format = format
        return

class DfConversationManager:
    def __init__(self, logger=logging.getLogger("rich"), project_id='aifo-project1', session_id='session_id', language_code='en'):
        self.log = logger
        self.project_id = project_id
        self.session_id = session_id
        self.language_code = language_code
        self.params = dict()

    def store_parameters(self, response_arguments):
        if response_arguments:
            for param, value in response_arguments.items():
                self.params[param] = value

    def sendMessage(self, message):
        response = ""
        response_intent = ""
        response_parameters = dict()
       
        response = self.session_client.detect_intent(
            session=self.session, query_input=dialogflow.QueryInput(text=dialogflow.TextInput(text=message, language_code=self.language_code))
        )
        response_text = response.query_result.fulfillment_text
        intent = response.query_result.intent.display_name
        parameters = response.query_result.parameters
        self.store_parameters 

        return response_text, intent, parameters