import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os

root = tk.Tk()
root.title("Course")
root.geometry("1400x1800")

def go_back1():
        os.system('python home.py')
        root.destroy()

required_fields = ["Digital Marketing", "Business Analytics", "Project Management", "Operations Management", "HR Management", "IT Management", "Business Management"]

bgimg = tk.PhotoImage(file="bgimg.png")
limg = tk.Label(root, image=bgimg)
limg.pack()

arrow= tk.PhotoImage(file="arrow1.png")
arrow_button = tk.Button(root, image=arrow, command=go_back1)
arrow_button.place(x=10, y=55)

heading = tk.Label( text='COURSE', fg='#ad74b8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=90, y=60)

img= tk.PhotoImage(file='logo4.png')
tk.Label(root,image=img).place(x=700,y=200)

var =tk.StringVar(value="0")
g1 = tk.Radiobutton (root,text = "Digital Marketing ",variable = var, value = "Digital Marketing .",font = "time 15")
g1.place (x =150, y = 180)

g2 = tk.Radiobutton (root,text = "Business Analytics ",variable = var, value = "Business Analytics .",font = "time 15")
g2.place (x = 150, y = 230)

g3 = tk.Radiobutton (root,text =" Project Management ",variable = var, value = "Project Management .",font = "time 15")
g3.place (x = 150, y = 280)

g4 = tk.Radiobutton (root,text =" Operations Management ",variable = var, value = "Operations Management .",font = "time 15")
g4.place (x =150, y = 330)

g5 = tk.Radiobutton (root,text =" HR Management ",variable = var, value = "HR Management .",font = "time 15")
g5.place (x =150, y = 380)

g6 = tk.Radiobutton (root,text =" IT Management ",variable = var, value = "IT Management .",font = "time 15")
g6.place (x =150, y = 430)

g7 = tk.Radiobutton (root,text =" Business Management ",variable = var, value = "Business Management .",font = "time 15")
g7.place (x =150, y = 480)


def go_back():
    if var.get() == "0":
        messagebox.showwarning("Select a Course", "Please select a course before proceeding")
    else:
        os.system('python home.py')
        root.destroy()

submit_button = tk.Button(root, text="OK",command=go_back, font="arial 13 bold", bg="#ae75b9", fg="white", width=20, height=2)
submit_button.place(x=400, y=550)

root.mainloop()