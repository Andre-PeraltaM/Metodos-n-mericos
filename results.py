from tkinter import *


def Results(data):
    root = Tk()
    root.geometry("1100x500")
    root.config(background="#213141")
    root.title("Resultados")
    root.resizable(False, False)

    frame = Frame(root)
    frame.pack(fill="both", expand=1)
    frameDos = Frame(frame, width=550, height=500)
    frameDos.pack(side=LEFT)
    frameDos.config(bg="blue")
    frameTres = Frame(frame, width=550, height=500)
    frameTres.pack(side=LEFT)
    frameTres.config(bg="lightblue")

    frame.pack(side=LEFT)
    frameDos.pack(side=RIGHT)

    textArea = Text(frameTres)
    textArea.pack(fill=Y)
    textArea.configure(font=("Courier", 16, "italic"))
    textArea.insert(INSERT, data)

    root.mainloop()
