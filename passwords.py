from main import *


class mainMenu:
    def __init__(self):
        window = tk.Tk()
        # Widget Start
        window.title("Test Window Name")
        window.geometry("250x250")
        btn1 = tk.Button(window, bg="#bec5c4", font="Arial", text="Process Kill Button", command=window.destroy)
        btn1.grid()
        # Widget End
        window.mainloop()