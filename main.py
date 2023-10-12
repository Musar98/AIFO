import tkinter


class RootConfig:
    def __init__(self, main):
        self.root = main
        self.title = main.title("Tkinter-Class")
        self.config = main.configure(bg="black", )
        self.x = int(main.winfo_screenwidth() / 2 - (main.winfo_reqwidth() / 2))
        self.y = int(main.winfo_screenheight() / 3 - (main.winfo_reqheight() / 2))
        self.geometry = main.geometry(f"+{self.x}+{self.y}")


if __name__ == "__main__":
    root = tkinter.Tk()
    RootConfig(root)
    root.mainloop()
