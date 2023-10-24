import os
import tkinter
import argparse
import logging
from rich.logging import RichHandler
from aifo.gui.ChatWindow import ChatWindow


API_KEY = "/home/musa/gclk/aifo-project1-dac1e93933c0.json"
# "C:/Users/mrcls/OneDrive - schbm/schubm/private/aifo-project1-dac1e93933c0.json"

def main():
    logging.basicConfig(
        level="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )
    log = logging.getLogger("rich")
    
    parser = argparse.ArgumentParser(
                    prog='AIFO - AI Youtube Media Downloader',
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
    log.debug(args)
    log.info(f"setting API key env: GOOGLE_APPLICATION_CREDENTIALS={args.api_key}")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = API_KEY
    log.info(f"starting mode: cli_mode={args.cli_mode}")
    if args.cli_mode:
        start_cli_mode
    else:
        start_gui_mode()

# start program in gui mode
def start_gui_mode():
    root = tkinter.Tk()
    chat_window = ChatWindow(root)
    root.mainloop()

# start program in cli mode
def start_cli_mode():
    # TODO: implement cli mode
    return

# run main if called directly
if __name__ == "__main__":
    main()
