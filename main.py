import tkinter


class RootConfig:
    def __init__(self, main):
        self.root = main
        self.title = main.title("Chat Window")
        self.config = main.configure(bg="black")
        self.x = int(main.winfo_screenwidth() / 2 - (main.winfo_reqwidth() / 2))
        self.y = int(main.winfo_screenheight() / 3 - (main.winfo_reqheight() / 2))
        self.geometry = main.geometry("400x520+{}+{}".format(self.x, self.y))
        self.resizable = main.resizable(0, 0)

        self.chat_display = tkinter.Text(main, bg="black", fg="white", wrap=tkinter.WORD, state=tkinter.DISABLED,
                                         cursor='arrow', highlightcolor='black', highlightbackground='black')
        self.chat_display.pack(fill=tkinter.BOTH, expand=True)

        input_frame = tkinter.Frame(main)
        input_frame.pack(fill=tkinter.X)

        self.input_entry = tkinter.Entry(input_frame, bg="darkgrey", highlightcolor='grey')
        self.input_entry.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)

        send_button = tkinter.Button(input_frame, text="Send", background="darkgrey",
                                     command=self.send_message)
        send_button.pack(side=tkinter.RIGHT)

        self.input_entry.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        message = self.input_entry.get()
        if message:
            self.chat_display.config(state=tkinter.NORMAL)
            current_text = self.chat_display.get(1.0, tkinter.END)
            updated_text = "You: " + message + "\n" + current_text
            self.chat_display.delete(1.0, tkinter.END)
            self.chat_display.insert(tkinter.INSERT, updated_text)
            self.chat_display.config(state=tkinter.DISABLED)
            self.input_entry.delete(0, tkinter.END)


if __name__ == "__main__":
    root = tkinter.Tk()
    RootConfig(root)
    root.mainloop()
