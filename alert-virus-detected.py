from tkinter import *
from tkinter import messagebox

def show_alert():
    messagebox.showwarning("Virus Detected", "A virus has been detected on your system!")

root = Tk()
root.title("Virus Scanner")
root.geometry("300x200")

button = Button(root, text="Scan for Viruses", command=show_alert)
button.pack(pady=50)

root.mainloop()