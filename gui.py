from main import *
from passwords import *

def callback():
    filename = 'passwords' + '.py'
    os.system(filename)

class mainMenu:
    window = tk.Tk()
    # Widget Start
    window.title("Test Window Name")
    window.geometry("250x250")
    btn1 = tk.Button(window, bg="#bec5c4", font="Arial", text="Process Kill Button", command=window.destroy)
    btn1.grid()
    btn2 = tk.Button(window, bg="#bec5c4", font="Arial", text="Passwords", command=callback)
    btn2.grid()
    # Widget End
    window.mainloop()
