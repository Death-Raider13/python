from tkinter import *

root=Tk()
root.geometry("400x400")
root.title("Top A Window")


def top_window():
    top=Toplevel()
    top.title("Tops Window")
    top.geometry("200x200")
    labels=Label(top,text="This is a top window")
    labels.pack()

    top.mainloop()


label=Label(root, text="This is the main window")
button=Button(root, text="Open Top Window", command=top_window)

label.pack()
button.pack()

root.mainloop()