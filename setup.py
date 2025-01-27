from tkinter import *

def ok():
    entryinput = entry.get()
    print(entryinput)   

window = Tk()
window.geometry("300x100")

label = Label(window, text="Quick Print! Type something in and it will instantly print!")
label.pack()

entry = Entry(window)
entry.pack()

button = Button(window, text="Apply", command=ok)
button.pack()

window.mainloop()



