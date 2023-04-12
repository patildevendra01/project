import tkinter as tk
from PIL import ImageTk, Image
import os


root = tk.Tk()
root.title("GENERATE QR CODE FOR STUDENT INFORMATION FORM")
root.geometry("1450x1800")

icon_image = ImageTk.PhotoImage(Image.open("menu.png"))
icon1 = ImageTk.PhotoImage(Image.open("icon1.png"))

bg_image = ImageTk.PhotoImage(Image.open("bgimg.png"))
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

course_img=ImageTk.PhotoImage(Image.open("qr1.png"))
course_img_label = tk.Label(root, image=course_img)
course_img_label.place(x=600,y=160)

toggle_menu_fm = None
profile_menu_fm = None

def open_attendence():
    os.system('python attendence.py')
    root.destroy()
def open_course():
    os.system("python courses.py")
    root.destroy()
def change_pass():
    os.system("python change.py")
    root.destroy()

def toggle_menu():
    global toggle_menu_fm
    def collapse_toggle_menu():
        root.toggle_btn.config(image=icon_image)
        root.toggle_btn.config(command=toggle_menu)
        root.toggle_menu_fm.destroy()
        root.toggle_menu_fm = None

    if toggle_menu_fm:
        collapse_toggle_menu()
    else:
        toggle_menu_fm = tk.Frame(root, bg='#571a90')
        attendence_btn = tk.Button(toggle_menu_fm, text='Attendance', font=('Bold', 20), bd=0, bg='#a839ae', fg='white',activebackground='white', activeforeground= 'black',command=open_attendence)
        attendence_btn.place(x=20,y=20)

        course_btn = tk.Button(toggle_menu_fm, text='Course', font=('Bold', 20), bd=0, bg='#a839ae', fg='white',command=open_course,activebackground="white", activeforeground= 'black')
        course_btn.place(x=20,y=80)
        window_height = root.winfo_height()
        toggle_menu_fm.place(x=0 , y=100, height=window_height, width=200)

        root.toggle_btn.config(image=icon_image)
        root.toggle_btn.config(command=collapse_toggle_menu)

def logout():

    quit()

def profile_menu():
    global profile_menu_fm
    def collapse_profile_menu():
        profile_btn.config(command=profile_menu)
        root.profile_menu_menu.destroy()
        profile_menu_fm = None
    
    if profile_menu_fm:
        collapse_profile_menu()
    else:
        profile_menu_fm = tk.Frame(root, bg='#571a90')
        log_btn = tk.Button(profile_menu_fm, text='Change Password', font=('Bold', 15), bd=0, bg='#a839ae', fg='white',activebackground="white", activeforeground="black",command=change_pass)
        log_btn.place(x=20, y=20)

        logout_btn = tk.Button(profile_menu_fm, text='Log Out', font=('Bold', 15), bd=0, bg='#a839ae', fg='white',activebackground='white', activeforeground="black",command=logout)
        logout_btn.place(x=20, y=80)
        window_height = root.winfo_height()
        profile_menu_fm.place(x=1100, y=100, height=window_height, width=200)

        profile_btn.config(text='+')
        profile_btn.config(command=collapse_profile_menu)

head_frame = tk.Frame(root, bg='#a839ae')

toggle_btn = tk.Button(head_frame, image=icon_image, bg='#a839ae', fg="white", font=("Bold", 20), bd=0, activebackground="BLACK", activeforeground= "white",command=toggle_menu)
toggle_btn.pack(side=tk.LEFT)

title_lb = tk.Label(head_frame, text='Dashboard', bg='#a839ae',fg="white", font=("Bold", 20))
title_lb.pack(side=tk.LEFT)

profile_btn = tk.Button(head_frame, image=icon1, bg='#a839ae', fg="white", font=("Bold", 20), bd=0, activebackground="BLACK", activeforeground= "white",command=profile_menu)
profile_btn.pack(side=tk.RIGHT)

title_bb = tk.Label(head_frame, text='Profile', bg='#a839ae',fg="white", font=("Bold", 20))
title_bb.pack(side=tk.RIGHT)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=100)

def qr():
   os.system("python sample2.py")
qr_btn = tk.Button(root, text='Genrate QR Code',command=qr, font=('Bold', 18), bd=0, bg='#a839ae', fg='white', activebackground='white', activeforeground='black')
qr_btn.place(x=550, y=280)

root.mainloop()
