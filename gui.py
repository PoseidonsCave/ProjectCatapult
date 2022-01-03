from main import *
import passwords
import calculator

class mainMenu: 
    def callback(self): 
        passwords.mainMenu()
        calculator.mainMenu()
    def __init__(self):
        window = tk.Tk()
        # Widget Start
        window.title("Test Window Name")
        window.geometry("250x250")
        btn1 = tk.Button(window, bg="#bec5c4", font="Arial", text="Process Kill Button", command=window.destroy)
        btn1.grid()
        btn2 = tk.Button(window, bg="#bec5c4", font="Arial", text="Passwords", command=self.callback)
        btn2.grid()
        btn3 = tk.Button(window, bg="#bec5c4", font="Arial", text="Calculator", command=self.callback)
        btn3.grid()
        # Widget End
        window.mainloop()

mainMenu()
