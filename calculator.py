from imports import math
from imports import tk


class mainMenu:
    def __init__(self):
        window = tk.Tk()
        # Widget Start
        window.title("Calculator")
        window.geometry("250x250")
        btn1 = tk.Button(window, bg="#bec5c4", font="Arial", width=15, text="Process Kill Button", command=window.destroy)
        btn1.grid()
        # Widget End
        window.mainloop()