import tkinter as tk
import math
from gui import MainMenu

class calcMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.setup_window()
        self.create_widgets()
        self.window.mainloop()

    def setup_window(self):
        self.window.title("Calculator")
        self.window.geometry("250x250")

    def create_widgets(self, window):
        btn1 = self.create_button(window, "Redirect to Primary GUI", self.redirect_to_primary_gui)
        btn1.grid()

    def create_button(self, parent, text, command):
        return tk.Button(parent, bg="#bec5c4", font="Arial", width=25, text=text, command=command)

    def redirect_to_primary_gui(self):
        self.window.destroy()  # Close the current window
        primary_gui_window = tk.Tk()  # Create a new Tkinter window
        primary_gui = MainMenu(primary_gui_window)  # Create an instance of your PrimaryGUI class
        primary_gui_window.mainloop()

if __name__ == "__main__":
    app = calcMenu()
