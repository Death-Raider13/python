from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


root=Tk()
root.title("Denominator Calculator")
root.configure(bg="lightgray")
root.geometry("400x300")

upload=Image.open("cloudspark.jpg")
upload=upload.resize((400,300))
upload=ImageTk.PhotoImage(upload)
label=Label(root, image=upload, bg="lightgray")
label.place(x=100, y=100)

label1=Label(root, text="hey user!, welcome to the denominator calculator", font=("Arial", 12), bg="lightgray")
label1.place(relx=0.5, y=0.1, anchor=CENTER)


def msg():
    msgBox= messagebox.showinfo("Denominator Calculator", "This calculator will help you find the denominator of a fraction. Please enter the numerator and the denominator in the respective fields and click on the 'Calculate' button to get the result.")
    if msgBox =='ok':
        topwin()

button1 =Button(root, text= "Lets get started!", font=("Arial", 12), bg="lightblue", fg="black", command=msg)
button1.place(x=150, y=200)

def topwin():
    top = Toplevel(root)
    top.title("Denominator Calculator")
    top.configure(bg="Beige")
    top.geometry("400x300")


    label=Label(top, text="Enter total amount", font=("Arial", 12), bg="Beige")
    entry=Entry(top, font=("Arial", 12), bg="white", fg="black")
    lbl1=Label(top,text="Here are number of notes for each denomination", font=("Arial", 12), bg="Beige")

    l1=Label(top, text=" 2000", font=("Arial", 12), bg="Beige")
    l2=Label(top, text=" 500", font=("Arial", 12), bg="Beige")
    l3=Label(top, text=" 100", font=("Arial", 12), bg="Beige")

    t1=Entry(top, font=("Arial", 12), bg="white", fg="black")
    t2=Entry(top, font=("Arial", 12), bg="white", fg="black")
    t3=Entry(top, font=("Arial", 12), bg="white", fg="black")

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount = amount % 2000
            note500 = amount // 500
            amount = amount % 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer amount.")

    btn=Button(top, text="Calculate", font=("Arial", 12), bg="lightblue", fg="black", command=calculator)

    label.place(x=20, y=20)
    entry.place(x=20, y=60)
    btn.place(x=240, y=100)
    lbl1.place(x=240, y=160)

    l1.place(x=20, y=100)
    l2.place(x=20, y=140)
    l3.place(x=20, y=180)

    t1.place(x=120, y=100)
    t2.place(x=120, y=140)
    t3.place(x=120, y=180)


    top.mainloop()
root.mainloop()