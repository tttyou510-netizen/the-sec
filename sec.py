import tkinter as tk
from tkinter import messagebox  
#islam ahmed ramadan
def exit_app():

    root.destroy()


def normal_button_action():
   
    messagebox.showinfo("the button", "you click🟢")


root = tk.Tk()
root.title("My App   ")

myframe = tk.Frame(root, bg="light green", padx=200, pady=200)
myframe.pack(padx=10, pady=10)

label = tk.Label(myframe, text=" my app ", font="Helvetica 14 bold", fg="yellow", bg="light green")
label.pack(pady=10)

exit_button = tk.Button(
    myframe,
    text=" exit",
    command=exit_app,  
    font=("Helvetica", 12, "bold"),
    fg="yellow",     
    bg="green",       
    padx=15,
    pady=5,
    relief=tk.RAISED
)
exit_button.pack(side=tk.LEFT, padx=40)

normal_button = tk.Button(
    myframe,
    text="click",
    command=normal_button_action, 
    font=("Helvetica", 12, "bold"),
    fg="green",         
    bg="yellow",       
    padx=15,
    pady=5,
    relief=tk.RAISED
)
normal_button.pack(side=tk.RIGHT, padx=40)



root.mainloop()