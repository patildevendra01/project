import sqlite3
import qrcode

# Connect to the database
conn = sqlite3.connect('data2.db')
c = conn.cursor()

# Retrieve data for a specific student
name = 1  # replace with the ID of the desired student
c.execute("SELECT * FROM student_info WHERE name=?", (name))
record = c.fetchone()

# Generate the QR code for the record
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(str(record))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.show()
