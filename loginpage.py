import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import sqlite3

root = tk.Tk()
root.title('GENRATE QR CODE FOR STUDENT INFORMATION ')
root.geometry("1450x1800")

bgimg = ImageTk.PhotoImage(file="bgimg.png")
limg = tk.Label(root, image=bgimg)
limg.pack()

def signin():
    username = user.get()
    password = code.get()
    if username == '' or password == '':
        messagebox.showerror('Error', 'Please fill in both username and password')
    else:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user_data = c.fetchone()
        conn.close()

        if user_data:
            os.system('python home.py')
            root.destroy()
        else:
            messagebox.showerror('Error', 'Invalid username or password')

def next():
    os.system('python regi.py')
    root.destroy()

def on_enter_user(e):
    if user.get() == 'Username':
        user.delete(0, 'end')

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, 'Username')

def check_fields(event):
    if user.get() and code.get():
        button.config(state="normal")
    else:
        button.config(state="disabled")

img = tk.PhotoImage(file='lgimg.png')
tk.Label(root, image=img).place(x=85, y=160)

frame = tk.Frame(root, width=350, height=350, bg="white")
frame.place(x=645, y=145)

heading = tk.Label(frame, text='Welcome', fg='#ba79bd', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

user = tk.Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_user)
user.bind("<FocusOut>", on_leave_user)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter_code(e):
    if code.get() == 'Password':
        code.delete(0,'end')

def on_leave_code(e):
    if code.get() == '':
        code.insert(0, "Password")

code = tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei uI Light', 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enter_code)
code.bind('<FocusOut>', on_leave_code)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

button = tk.Button(frame, width=39, pady=7, text='login', bg='#ba79bd', fg='white', border=0, state="disabled",command=signin)
button.place(x=35, y=204)

label = tk.Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UA Light', 9))
label.place(x=75, y=270)

sign_up = tk.Button(frame, width=6, text='sign up', border=0, bg='white', cursor='hand2', fg="#ba79bd", command=next)
sign_up.place(x=215, y=270)

user.bind("<KeyRelease>", check_fields)
code.bind("<KeyRelease>", check_fields)

root.mainloop()
