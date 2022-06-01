from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("STEGANOGRAPHY DATA HIDER ")
root.geometry("700x600+250+180")
root.resizable(False, False)
root.configure(bg = "black")

####FUNCTIONS#####
def showimage():
    global filename
    filename =filedialog.askopenfilename(initialdir=os.getcwd(),
                                         title='Select Image File',
                                         filetype=(("PNG file","*.png"),
                                                   ("JPG file","*.jpg"),
                                                   ("All files","*.txt")))
    img= Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image = img

def Hide():
    global secret
    # global text1
    message=text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)

def Show():
   clear_message = lsb.reveal(filename)
   text1.delete(1.0,END)
   text1.insert(END,clear_message)

def save():
    secret.save("hidden.png")


#icon
image_icon =PhotoImage(file ="img.png")
root.iconphoto(False,image_icon)
#logo
logo = PhotoImage(file ="lg.png")
Label(root,
      image=logo,
      bg="white"
      ).place(x=10,y=0)
Label(root,text ="HIDE SECRET MESSAGE",
      bg ="#2d4155",
      fg="white",
      font="arial 26 bold"
      ).place(x=250,y=10)

#first frame
f = Frame(root,
          bd=3,
          bg ="black",
          width=340,
          height=280,
          relief = GROOVE
          )
f.place(x=10,y=220)

lbl =Label(f,bg="black")
lbl.place(x=40,y=10)
#Second frame
frame2 = Frame(root,
               bd=3,
               bg ="white",
               width=340,
               height=280,
               relief=GROOVE
               )
frame2.place(x=350,y=220)
text1= Text(frame2,
            font="Robote20",
            bg="white",
            fg ="black",
            relief=GROOVE
            )
text1.place(x=0,
            y=0,
            width=320,
            height=295,
            # wrap = WORD
            )
scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320,
                 y=0,
                 height=300
                 )
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame
frame3 = Frame(root,
               bd=3,
               bg="#2f4155",
               width=340,
               height=100,
               relief= GROOVE
               )
frame3.place(x=10,y=500)

Button(frame3,text="Open Image", width=10,height=1,font="arial 14 bold",command=showimage).place(x=20,y=40)
Button(frame3,text="Save Image", width=10,height=1,font="arial 14 bold",command=save).place(x=200,y=40)
Label(frame3,text="Picture, Image, Photo File",bg ="#2f4155",fg="yellow",font="arial 8").place(x=20,y=5)

#forth frame
frame4 = Frame(root,
               bd=3,
               bg="#2f4155",
               width=340,
               height=100,
               relief= GROOVE
               )
frame4.place(x=360,y=500)

Button(frame4,text="Hide Data", width=10,height=1,font="arial 14 bold",command=Hide).place(x=20,y=40)
Button(frame4,text="Show Data", width=10,height=1,font="arial 14 bold",command=Show).place(x=200,y=40)
Label(frame4,text="Picture, Image, Photo File",bg ="#2f4155",fg="yellow",font="arial 8").place(x=20,y=5)


#run the window
root.mainloop()