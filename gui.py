from imports import *
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
        btn1 = tk.Button(window, bg="#bec5c4", font="Arial", width=15, text="Process Kill Button", command=window.destroy)
        btn2 = tk.Button(window, bg="#bec5c4", font="Arial", width=15, text="Passwords", command=self.callback)
        btn3 = tk.Button(window, bg="#bec5c4", font="Arial", width=15, text="Calculator", command=self.callback)
        
        btn1.grid()
        btn2.grid()
        btn3.grid()
        # Widget End
        window.mainloop()

mainMenu()
