import tkinter
mw = tkinter.Tk()
btn = tkinter.Button(mw, text="OK")

def button_handler():
    return 7/0

btn.config(command= button_handler)
btn.pack()
mw.mainloop()