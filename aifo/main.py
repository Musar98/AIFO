
import argparse
import tkinter
import os
from aifo.gui.ChatWindow import ChatWindow

API_KEY = "/home/musa/gclk/aifo-project1-dac1e93933c0.json"
# "C:/Users/mrcls/OneDrive - schbm/schubm/private/aifo-project1-dac1e93933c0.json"


def main():
    parser = argparse.ArgumentParser(
                    prog='AI Youtube Media Downloader',
                    description='Download Youtube Media with AI',
                    epilog='Enjoy the program! :)')
    parser.add_argument("--api_key",
                        type=str,
                        help="Path to API key json file",
                        default=API_KEY)
    parser.add_argument("--cli_mode",
                        type=bool,
                        help="Start program in CLI mode",
                        default=False)
    args = parser.parse_args()
    print(args)
    start_gui_mode()


def start_gui_mode():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = API_KEY
    root = tkinter.Tk()
    chat_window = ChatWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
