import tkinter as tk
import random
import string
def generate_password():
    length = int(length_entry.get())
    if length < 1:
        password_var.set("Length should be at least 1")
        return
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_var.set(password)
root = tk.Tk()
root.title("Password Generator")
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var)
password_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
root.mainloop()
