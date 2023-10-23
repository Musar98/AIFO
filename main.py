import tkinter
from dialogflow_client import interact_with_dialogflow


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

        send_button = tkinter.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tkinter.RIGHT)

        self.input_entry.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        message = self.input_entry.get()
        if message:
            self.chat_display.config(state=tkinter.NORMAL)
            current_text = self.chat_display.get(1.0, tkinter.END)
            if current_text.strip():
                updated_text = current_text.rstrip() + "\nYou: " + message
            else:
                updated_text = "You: " + message
            self.chat_display.delete(1.0, tkinter.END)
            self.chat_display.insert(tkinter.END, updated_text)
            self.chat_display.config(state=tkinter.DISABLED)
            self.input_entry.delete(0, tkinter.END)

            self.input_entry.config(state=tkinter.DISABLED)

            self.root.after(100, self.send_message_to_dialogflow, message)

    def send_message_to_dialogflow(self, message):
        res = interact_with_dialogflow('aifo-project1', "session_id", message)
        self.update_chat_with_response(res[1])

        self.input_entry.config(state=tkinter.NORMAL)

    def update_chat_with_response(self, response):
        self.chat_display.config(state=tkinter.NORMAL)
        current_text = self.chat_display.get(1.0, tkinter.END)
        updated_text = current_text.rstrip() + "\nBot: " + response
        self.chat_display.delete(1.0, tkinter.END)
        self.chat_display.insert(tkinter.END, updated_text)
        self.chat_display.config(state=tkinter.DISABLED)


if __name__ == "__main__":
    root = tkinter.Tk()
    RootConfig(root)
    root.mainloop()
