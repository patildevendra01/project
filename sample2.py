import qrcode
from PIL import ImageTk, Image
import sqlite3
import tkinter as tk

conn = sqlite3.connect('data1.db')
c = conn.cursor()

root = tk.Tk()

def display_qrcode():
    try:
        # Get the data from the database
        data = c.execute("SELECT * FROM student_info").fetchall()
        # Create a QR code with the data
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        for d in data:
            qr.add_data(str(d))
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        # Display the QR code in a new window
        new_window = tk.Toplevel()
        new_window.title("QR Code")
        # Resize the image to fit the window
        width, height = img.size
        if width > 500 or height > 500:
            img = img.resize((500, 500))
        # Convert the image to PhotoImage format
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(new_window, image=photo)
        label.image = photo
        label.pack()
    except Exception as e:
        # Handle any exceptions that occur during execution
        tk.messagebox.showerror("Error", str(e))

# Create a button to display the QR code
button = tk.Button(root, text="Display QR Code", command=display_qrcode)
button.pack()

root.mainloop()

# Close the database connection when the program exits
conn.close()
