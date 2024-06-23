import tkinter as tk
import passwords
import calculator

class MainMenu:
    def __init__(self, root):
        self.root = root
        root.title("Test Window Name")
        root.geometry("250x250")

        self.create_widgets()

    def create_widgets(self):
        btn1 = self.create_button("Process Kill Button", self.root.destroy)
        btn2 = self.create_button("Passwords", self.open_passwords)
        btn3 = self.create_button("Calculator", self.open_calculator)

        btn1.grid()
        btn2.grid()
        btn3.grid()

    def create_button(self, text, command):
        return tk.Button(self.root, bg="#bec5c4", font="Arial", width=15, text=text, command=command)

    def open_passwords(self):
        passwords.passwordMenu()

    def open_calculator(self):
        calculator.calcMenu()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()