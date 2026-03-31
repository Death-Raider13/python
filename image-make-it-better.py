from tkinter import*
from PIL import Image, ImageTk


root = Tk()
root.title("Image Make It Better")
root.geometry("500x500")

upload=Image.open("cloudspark.jpg")

image=ImageTk.PhotoImage(upload)

label=Label(root,image=image, height=300, width=300)
label.place(x=50,y=50)

label2=Label(root,text="This is how u add image to tkinter", font=("Arial", 20))
label2.place(x=40,y=360)


root.mainloop()