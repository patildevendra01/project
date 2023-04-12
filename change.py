import tkinter as tk
from PIL import Image, ImageTk
import os
import sqlite3

root = tk.Tk()
root.title('GENERATE QR CODE FOR STUDENT INFORMATION')
root.geometry("1450x1800")

bgimg = ImageTk.PhotoImage(file="bgimg.png")
limg = tk.Label(root, image=bgimg)
limg.pack()

frame = tk.Frame(root, width=350, height=350, bg="white")
frame.place(x=645, y=145)

img = ImageTk.PhotoImage(file='lgimg.png')
tk.Label(root, image=img).place(x=75, y=160)

heading = tk.Label(frame, text='Change Password', fg='#ad74b8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=20, y=5)

def change_password():
    email = email_entry.get()
    username = username_entry.get()
    new_password = new_password_entry.get()

    conn = sqlite3.connect('data1.db')
    c = conn.cursor()
    c.execute("UPDATE information SET password = ? WHERE email = ? AND username = ?", (new_password, email, username))
    conn.commit()
    conn.close()

    print(f"Password for {username} with email id {email} has been updated to {new_password}")
    email_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    new_password_entry.delete(0, tk.END)

def clear_fields():
    username_entry.delete(0, 'end')
    new_password_entry.delete(0, 'end')
    email_entry.delete(0, 'end')

email_label = tk.Label(frame, text="Emai")
email_entry = tk.Entry(frame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light", 11))
email_entry.place(x=30, y=150)
email_entry.insert(0,'Email')
def clear_email_text(event):
    if email_entry.get() == 'Email':
        email_entry.delete(0, 'end')
email_entry.bind('<Button-1>', clear_email_text)

username_label = tk.Label(frame, text="Username:")
username_entry = tk.Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
username_entry.place(x=30, y=80)
username_entry.insert(0, 'Username')
def clear_username_text(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, 'end')
username_entry.bind('<Button-1>', clear_username_text)

new_password_label = tk.Label(frame, text="New Password:")
new_password_entry = tk.Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
new_password_entry.place(x=30, y=220)
new_password_entry.insert(0, 'New Password')
def clear_password_text(event):
    if new_password_entry.get() == 'New Password':
        new_password_entry.delete(0, 'end')
new_password_entry.bind('<Button-1>', clear_password_text)

submit=tk.Button(frame, width=39, pady=7, text='Submit', bg='#ad74b8', fg='white', border=0 , command=change_password)
submit.place(x=35, y=275)

def go_back():
    os.system('python home.py')
    root.destroy()

arrow= tk.PhotoImage(file="arrow1.png")
arrow_button = tk.Button(root, image=arrow, command=go_back)
arrow_button.place(x=30, y=30)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

root.mainloop()