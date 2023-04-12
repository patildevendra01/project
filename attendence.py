import tkinter as tk1
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sqlite3

root = tk1.Tk()
root.title("Student  Attendance Form")
root.geometry("1400x1800")

bgimg = tk1.PhotoImage(file="bgimg.png")
limg = tk1.Label(root, image=bgimg)
limg.pack()

l1 = tk1.Label (root, text = "Student Attendance", font = "time 20 bold")
l1.place (x = 90, y= 80)

img= tk1.PhotoImage(file='logo3.png')
tk1.Label(root,image=img).place(x=750,y=150)

def go_back():
    os.system('python home.py')
    root.destroy()

arrow= tk1.PhotoImage(file="arrow1.png")
arrow_button = tk1.Button(root, image=arrow, command=go_back)
arrow_button.place(x=30, y=7)

l2 = tk1.Label (root, text = " Name:",font = "time 15 bold")
l2.place(x =90, y = 220)

e1 = tk1.Entry(root, width = 30, bd = 3,)
e1.place(x = 260, y = 220)

l3 = tk1.Label (root, text = "Roll No:",font = "time 15 bold")
l3.place (x = 90, y = 280)

e2 = tk1.Entry (root, width = 30, bd = 3,)
e2.place (x = 260, y = 280)

l4 = tk1.Label (root, text = "Status:",font = "time 15 bold")
l4.place (x = 90, y = 340)

var =tk1.StringVar(value="0")
g1 = tk1.Radiobutton (root,text = "present .",variable = var, value = "Present .",font = "time 15")
g1.place (x = 260, y = 340)

g2 = tk1.Radiobutton (root,text = "Absent .",variable = var, value = "Absent .",font = "time 15")
g2.place(x = 360, y = 340)
def submit():
    if e1.get() == "" or e2.get() == "" or var.get() == "0":
        messagebox.showerror("Error", "Please fill all the entries")

    else:
        os.system('python home.py')
        root.destroy()

submit_button = tk1.Button(root, text="Submit", command=submit, font="arial 13 bold", bg="#ae75b9", fg="white", width=20, height=2)
submit_button.place(x=550, y=500)

root.mainloop()