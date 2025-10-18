import tkinter as tk
from tkinter import messagebox
import string
import secrets


#  Check Password Strength
def check_strength(password): 
    if not password:
        return "Please enter a password."
    elif len(password) < 8:
        return "Weak (Too short)"
    elif password.isalpha(): 
        return "Weak"
    elif any(c.isdigit() for c in password) and password.isalnum():
        return "Medium"
    elif (
        any(c.isdigit() for c in password)
        and any(c.isalpha() for c in password)
        and any(not c.isalnum() for c in password)
        and len(password) > 12
    ):
        return "Strong"
    else:
        return "Medium"


# Generate Random Password
def generate_password():
    length = 8
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    messagebox.showinfo("Password Generated", "New password generated successfully!")


# Copy Password
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")


# Display Strength
def display_strength():
    password = password_entry.get()
    strength = check_strength(password)
    result_label.config(text=f"Password Strength: {strength}")


# UI Setup (Tkinter)

root = tk.Tk()
root.title("Password Strength Checker & Generator")
root.geometry("600x350")
root.config(bg="#0f172a")

title_label = tk.Label(
    root, text="⚡ Power Up Your Passwords — Check & Generate Like a Pro!", 
    font=("Helvetica", 14, "bold"), fg="#38bdf8", bg="#0f172a"
)
title_label.pack(pady=30)
#input
inp_frame=tk.Frame(root,bg="#0f172a")
inp_frame.pack(pady=15)
inp_label = tk.Label(inp_frame, text="Password: ", font=("Helvetica", 10), fg="#e2e8f0", bg="#0f172a")
inp_label.grid(row=0, column=0)
password_entry = tk.Entry(inp_frame, width=40, show="*", font=("Helvetica", 12))
password_entry.grid(row=0, column=1)

# Buttons
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=10)

check_btn = tk.Button(btn_frame, text="Check Strength", command=display_strength, width=15, bg="#38bdf8")
check_btn.grid(row=0, column=0, padx=15)

gen_btn = tk.Button(btn_frame, text="Generate Password", command=generate_password, width=18, bg="#22c55e")
gen_btn.grid(row=0, column=1, padx=15)

copy_btn = tk.Button(btn_frame, text="Copy", command=copy_password, width=10, bg="#facc15")
copy_btn.grid(row=0, column=2, padx=15)

# Strength Display
result_label = tk.Label(root, text="Password Strength: ", font=("Helvetica", 12), fg="#e2e8f0", bg="#0f172a")
result_label.pack(pady=20)

# Show/Hide Password Option
def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

show_var = tk.BooleanVar()
show_check = tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password, bg="#0f172a",
             fg="#e2e8f0",selectcolor="#1e293b")
show_check.pack()

root.mainloop()
