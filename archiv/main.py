import tkinter
import sys
import os
from gui.ChatWindow import ChatWindow


API_KEY = "/home/musa/gclk/aifo-project1-dac1e93933c0.json"
# "C:/Users/mrcls/OneDrive - schbm/schubm/private/aifo-project1-dac1e93933c0.json"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        api_key_arg = sys.argv[1]
        if type(api_key_arg) is str:
            API_KEY = api_key_arg
        else:
            sys.exit("API key must be a string")

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = API_KEY
    root = tkinter.Tk()
    chat_window = ChatWindow(root)
    root.mainloop()
