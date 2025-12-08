# islam ahmed ramadan shroud
# 2 سكشن بسملة احمد سكشن 

from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Sign Up")
win.geometry("450x520")
win.config(bg="#0870f0")

Label(win, text=" Enter your Account", font=("Calibri", 30, "bold"), bg="#eef5ef").pack(pady=20)

f = Frame(win, bg="#16a567")
f.pack()

def add_field(text, show=None):
    Label(f, text=text, font=("Calibri",14), bg="#eef5ef").pack(anchor="w")
    e = Entry(f, font=("Calibri", 14), width=28, show=show)
    e.pack(pady=5)
    return e

name = add_field("Enter Name:")
mail = add_field(" Enter Email:")
pw = add_field("Enter Password:", show="•")
cpw = add_field(" Enter Confirm Password:", show="•")

def register():
    if not name.get() or not mail.get() or not pw.get() or not cpw.get():
        return messagebox.showerror("Error", "All fields are required.")
    if pw.get() != cpw.get():
        return messagebox.showerror("Error", "Passwords do not match.")
    messagebox.showinfo("Success", f"Account created for {name.get()}")

Button(win, text="Register", width=15, font=("Calibri", 13, "bold"),
    bg="#4a84d8", fg="white", command=register).pack(pady=25)

win.mainloop()
