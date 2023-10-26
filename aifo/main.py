import os
import tkinter
import argparse
import logging

from pathlib import Path
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
        epilog='Enjoy the program! :)'
    )
    parser.add_argument(
        "--api_key",
        type=str,
        default=API_KEY,
        help="Path to API key json file"
    )
    parser.add_argument(
        "--cli_mode",
        "-c",
        action="store_true",
        help="Start program in CLI mode"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output"
    )
    args = parser.parse_args()

    if args.verbose:
        log.level = 10
        log.debug("enabled verbose logging")

    downloads_folder = Path.home() / "Downloads"
    log.info(f"downloads={downloads_folder}")

    log.info(f"setting API key env: GOOGLE_APPLICATION_CREDENTIALS={args.api_key}")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = args.api_key
    log.info(f"starting mode: cli_mode={args.cli_mode}")

    if args.cli_mode:
        start_cli_mode
    else:
        start_gui_mode()
        return


def start_gui_mode():
    root = tkinter.Tk()
    chat_window = ChatWindow(root)
    root.mainloop()


def start_cli_mode():
    # TODO: implement cli mode
    return


if __name__ == "__main__":
    main()
