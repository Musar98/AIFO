import tkinter
from aifo.clients.dialogflow_client import interact_with_dialogflow


class ChatWindowFunctions:
    def __init__(self, chat_window):
        self.chat_window = chat_window

    def send_message_to_dialogflow(self, message):
        agent_response = interact_with_dialogflow('aifo-project1', "session_id", message)
        self.update_chat_with_response(agent_response[1])
        self.chat_window.input_entry.config(state=tkinter.NORMAL)

    def update_chat_with_response(self, response):
        self.chat_window.chat_display.config(state=tkinter.NORMAL)
        current_text = self.chat_window.chat_display.get(1.0, tkinter.END)
        updated_text = current_text.rstrip() + "\nBot: " + response
        self.chat_window.chat_display.delete(1.0, tkinter.END)
        self.chat_window.chat_display.insert(tkinter.END, updated_text)
        self.chat_window.chat_display.config(state=tkinter.DISABLED)
        self.chat_window.chat_display.yview_moveto(1.0)

    def send_message(self, event=None):
        message = self.chat_window.input_entry.get()
        if message:
            self.chat_window.chat_display.config(state=tkinter.NORMAL)
            current_text = self.chat_window.chat_display.get(1.0, tkinter.END)
            if current_text.strip():
                updated_text = current_text.rstrip() + "\nYou: " + message
            else:
                updated_text = "You: " + message
            self.chat_window.chat_display.delete(1.0, tkinter.END)
            self.chat_window.chat_display.insert(tkinter.END, updated_text)
            self.chat_window.chat_display.config(state=tkinter.DISABLED)
            self.chat_window.input_entry.delete(0, tkinter.END)

            self.chat_window.input_entry.config(state=tkinter.DISABLED)

            self.chat_window.root.after(100, self.send_message_to_dialogflow, message)
