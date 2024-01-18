import tkinter as tk
import math

class MainMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.setup_window()
        self.create_widgets()
        self.window.mainloop()

    def setup_window(self):
        self.window.title("Calculator")
        self.window.geometry("250x250")

    def create_widgets(self):
        btn1 = self.create_button("Process Kill Button", self.window.destroy)
        btn1.grid()

    def create_button(self, text, command):
        return tk.Button(self.window, bg="#bec5c4", font="Arial", width=15, text=text, command=command)

if __name__ == "__main__":
    app = MainMenu()
