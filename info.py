import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sqlite3
import qrcode
from PIL import Image
from tkcalendar import DateEntry

conn = sqlite3.connect('data1.db')
c = conn.cursor()

root = tk.Tk()
root.title("Student Information Form")
root.geometry("1400x1800")

c.execute('''CREATE TABLE IF NOT EXISTS student_info (
             name TEXT, prn TEXT, roll_no TEXT, birth_date TEXT, age TEXT,
             gender TEXT, mobile_no TEXT, gmail TEXT, faculty TEXT, address TEXT,
             class TEXT)''')
conn.commit()

required_fields = ["Name", "PRN", "Roll No", "Birth Date", "Age", "Gender", "Mobile No", "Gmail", "Faculty", "Address", "Class"]

bgimg = tk.PhotoImage(file="bgimg.png")
limg = tk.Label(root, image=bgimg)
limg.pack()

tk.Label(root, text="STUDENT INFORMATION FORM", font="arial 20 bold").place(x=400, y=50)

img= tk.PhotoImage(file='logo1.png')
tk.Label(root,image=img).place(x=950,y=30)

def go_back():
    os.system('python home.py')
    root.destroy()

arrow= tk.PhotoImage(file="arrow1.png")
arrow_button = tk.Button(root, image=arrow, command=go_back)
arrow_button.place(x=50, y=50)

tk.Label(root, text="NAME:", font="arial 13").place(x=90, y=180)
name_entry = tk.Entry(root, width=60,validate="key" )
name_entry.place(x=200, y=180)

tk.Label(root, text="PRN:", font="arial 13").place(x=90, y=230)
prn_entry = tk.Entry(root, width=60, validate="key")
prn_entry.place(x=200, y=230)

tk.Label(root, text="Roll No:", font="arial 13").place(x=700, y=230)
rollno_entry = tk.Entry(root, width=60, validate="key")
rollno_entry.place(x=820, y=230)

tk.Label(root, text="Birth Date:", font="arial 13").place(x=90, y=280)
birthdate_entry = DateEntry(root, width=60,validate="key")
birthdate_entry.place(x=200, y=280)

tk.Label(root, text="Age:", font="arial 13").place(x=700, y=280)
age_entry = tk.Entry(root, width=60, validate="key")
age_entry.place(x=820, y=280)

tk.Label(root, text="Gender:", font="arial 13").place(x=90, y=330)
gender_var = tk.StringVar(value="----select----")
gender_dropdown = tk.OptionMenu(root, gender_var, "Male", "Female", "Other")
gender_dropdown.config(width=8)
gender_dropdown.place(x=200, y=330)

tk.Label(root, text="Mobile No:", font="arial 13").place(x=700, y=330)
mobileno_entry = tk.Entry(root, width=60, validate="key")
mobileno_entry.place(x=820, y=330)

tk.Label(root, text="Gmail:", font="arial 13").place(x=90, y=380)
gmail_entry = tk.Entry(root, width=60,validate="key")
gmail_entry.place(x=200, y=380)

tk.Label(root, text="Faculty:", font="arial 13").place(x=700, y=380)
faculty_var = tk.StringVar(value="----select----")
faculty_dropdown = tk.OptionMenu(root, faculty_var, "ART", "COMMERCR", "SCIENCE")
faculty_dropdown.config(width=8)
faculty_dropdown.place(x=820, y=380)

tk.Label(root, text="Address:", font="arial 13").place(x=90, y=430)
address_entry = tk.Entry(root, width=60,validate="key")
address_entry.place(x=200, y=430)

tk.Label(root, text="Class:", font="arial 13").place(x=700, y=430)
Class_entry = tk.Entry(root, width=60,validate="key")
class_var = tk.StringVar(value="----select----")
class_dropdown = tk.OptionMenu(root, class_var, "FY", "SY", "TY")
class_dropdown.config(width=8)
class_dropdown.place(x=820, y=430)


def check_required_fields():
    for field in required_fields:
        entry = globals().get(f"{field.lower()}_entry")
        if not entry.get():
            messagebox.showerror("Error", f"{field} field is required")
            return False
        return True

def reset_fields():
    for field in required_fields:
        entry = globals().get(f"{field.lower()}_entry")
        entry.delete(0, tk.END)


def view_data():
    c.execute("SELECT * FROM student_info")
    data = c.fetchall()


def generate_qr_code(data):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img_path = os.path.join(os.getcwd(), "qrcode.png")
        img.save(img_path)
        qr_img = Image.open(img_path)
        qr_img.show()
def submit_data():
    if not check_required_fields():
        return

    name = name_entry.get()
    prn = prn_entry.get()
    roll_no = rollno_entry.get()
    birth_date = birthdate_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    mobile_no = mobileno_entry.get()
    gmail = gmail_entry.get()
    faculty = faculty_var.get()
    address = address_entry.get()
    class_ = class_var.get()

    data = f"Name: {name}\nPRN: {prn}\nRoll No: {roll_no}\nBirth Date: {birth_date}\nAge: {age}\nGender: {gender}\nMobile No: {mobile_no}\nGmail: {gmail}\nFaculty: {faculty}\nAddress: {address}\nClass: {class_}"
    generate_qr_code(data)

    c.execute('''INSERT INTO student_info (name, prn, roll_no, birth_date, age,
                        gender, mobile_no, gmail, faculty, address, class) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (name, prn, roll_no, birth_date, age, gender, mobile_no, gmail, faculty, address, class_))
    conn.commit()
    messagebox.showinfo("Success", "Data saved successfully")
    os.system("python home.py")

submit_button = tk.Button(root, text="Genertae QR Code", font="arial 14", command=submit_data)
submit_button.place(x=600, y=550)


root.mainloop()
