from google.cloud import dialogflow
import logging


def interact_with_dialogflow(project_id, session_id, text_query, language_code='en'):
    # Create a session client
    log = logging.getLogger("rich")
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    # Send a text query to the agent
    text_input = dialogflow.TextInput(text=text_query, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(request={'session': session, 'query_input': query_input})
    #log.info(response.query_result.parameters)
    #log.info(response)
    parameters = response.query_result.parameters
    if parameters:
        for param, value in parameters.items():
            print(f"Parameter '{param}': {value}")
    else:
        print("No parameters detected")
    # Return the response from the agent
    return response.query_result.query_text, response.query_result.fulfillment_text
