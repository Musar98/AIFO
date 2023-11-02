import tkinter
from aifo.gui.ChatWindowFunctions import ChatWindowFunctions


class ChatWindow:
    def __init__(self, main):
        self.root = main
        self.chat_window_functions = ChatWindowFunctions(self)
        self.title = main.title("Chat Window")
        self.config = main.configure(bg="black")
        self.x = int(main.winfo_screenwidth() / 2 - (main.winfo_reqwidth() / 2))
        self.y = int(main.winfo_screenheight() / 3 - (main.winfo_reqheight() / 2))
        self.geometry = main.geometry("400x520+{}+{}".format(self.x, self.y))

        self.chat_display = tkinter.Text(main, bg="black", fg="white", wrap=tkinter.WORD, state=tkinter.DISABLED,
                                         cursor='arrow', highlightcolor='black', highlightbackground='black')
        self.chat_display.pack(fill=tkinter.BOTH, expand=True)

        input_frame = tkinter.Frame(main)
        input_frame.pack(fill=tkinter.X)

        self.input_entry = tkinter.Entry(input_frame, bg="darkgrey", highlightcolor='grey')
        self.input_entry.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)

        send_button = tkinter.Button(input_frame, text="Send", command=self.chat_window_functions.update_chat_window)
        send_button.pack(side=tkinter.RIGHT)

        self.input_entry.bind("<Return>", self.chat_window_functions.update_chat_window)
