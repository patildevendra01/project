import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import sqlite3
import re
import os

root = tk.Tk()
root.title('Login')
root.geometry("1450x1800")

def create_table():
    conn=sqlite3.connect('data1.db')
    c=conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='information'")
    if not c.fetchone():
        c.execute("CREATE TABLE information(username TEXT, password TEXT, email TEXT)")
    conn.commit()
    conn.close()

def save_data(username, password, email):
    if not username or not password or not email:
        messagebox.showerror("Error", "Please fill all the fields.")
        return
    elif len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long.")
        return
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Please enter a valid email address.")
        return

    try:
        conn=sqlite3.connect('data1.db')
        c=conn.cursor()
        c.execute('INSERT INTO information(username,password,email) VALUES (?,?,?)',(username, password, email))
        conn.commit()
    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Error", "An error occurred. Please try again.")
    finally:
        conn.close()

    conn=sqlite3.connect('data1.db')
    c=conn.cursor()
    c.execute('SELECT * FROM information')
    data = c.fetchall()
    conn.close()

    if len(data) == 0:
        messagebox.showerror("Error", "Please fill all the fields.")
    else:
        os.system('python info.py')
        root.destroy()

def clear_fields():
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    email_entry.delete(0, 'end')

bgimg = ImageTk.PhotoImage(file="bgimg.png")
limg = tk.Label(root, image=bgimg)
limg.pack()

def go_back():
    os.system('python loginpage.py')
    root.destroy()

arrow= tk.PhotoImage(file="arrow1.png")
arrow_button = tk.Button(root, image=arrow, command=go_back)
arrow_button.place(x=30, y=30)


frame = tk.Frame(root, width=350, height=350, bg="white")
frame.place(x=645, y=145)

img = ImageTk.PhotoImage(file='lgimg.png')
tk.Label(root, image=img).place(x=75, y=160)

heading = tk.Label(frame, text='Create your account', fg='#ad74b8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=20, y=5)

username=tk.StringVar()
username_entry = tk.Entry(frame, width=25, fg="black", border=0, bg="white", textvariable=username, font=("Microsoft YaHei UI Light", 11))
username_entry.place(x=30, y=80)
username_entry.insert(0, 'Username')
def clear_username_text(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, 'end')
username_entry.bind('<Button-1>', clear_username_text)

password=tk.StringVar()
password_entry = tk.Entry(frame, width=25, fg='black', border=0, bg="white",textvariable=password, font=('Microsoft Yahei uI Light', 11), show='*')
password_entry.place(x=30, y=150)
password_entry.insert(0, "Password")
def clear_password_text(event):
    if password_entry.get() == 'Password':
        password_entry.delete(0, 'end')
password_entry.bind('<Button-1>', clear_password_text)

email=tk.StringVar()
email_entry = tk.Entry(frame, width=25, fg="black", border=0, bg="white", textvariable=email,font=("Microsoft YaHei UI Light", 11))
email_entry.place(x=30, y=220)
email_entry.insert(0, 'Email')
def clear_email_text(event):
    if email_entry.get() == 'Email':
        email_entry.delete(0, 'end')
email_entry.bind('<Button-1>', clear_email_text)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

submit=tk.Button(frame, width=39, pady=7, text='Submit', bg='#ad74b8', fg='white', border=0 , command= lambda: save_data(username.get(), password.get(), email.get()))
submit.place(x=35, y=275)

create_table()

root.mainloop()