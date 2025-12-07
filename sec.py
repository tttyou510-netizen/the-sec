import tkinter as tk
from tkinter import messagebox
# Islam Ahmed Ramadan
#2 سكشن بسملة احمد سكشن 
BG_FRAME = "light green"
FG_LABEL = "yellow"
BG_BUTTON_1 = "green"  
FG_BUTTON_1 = "yellow"
BG_BUTTON_2 = "yellow" 
FG_BUTTON_2 = "green"
FONT_BOLD = ("Helvetica", 12, "bold") 

class CalculatorApp:
    def _init_(self, master):
        self.master = master
        master.title("Calculator App")

        self.current_expression = ""
        self.input_text = tk.StringVar()

        self.frame = tk.Frame(master, bg=BG_FRAME, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        self.input_field = tk.Entry(
            self.frame,
            textvariable=self.input_text,
            font=("Helvetica", 18, "bold"),
            fg=FG_LABEL,
            bg=BG_BUTTON_1, 
            justify='right',
            bd=5,
            relief=tk.SUNKEN,
            width=25
        )
        self.input_field.grid(row=0, column=0, columnspan=4, pady=10)
        self.input_field.insert(0, "0")

  
        buttons = [
            ('7', 1, 0, BG_BUTTON_2, FG_BUTTON_2), ('8', 1, 1, BG_BUTTON_2, FG_BUTTON_2),
            ('9', 1, 2, BG_BUTTON_2, FG_BUTTON_2), ('/', 1, 3, BG_BUTTON_1, FG_BUTTON_1),

            ('4', 2, 0, BG_BUTTON_2, FG_BUTTON_2), ('5', 2, 1, BG_BUTTON_2, FG_BUTTON_2),
            ('6', 2, 2, BG_BUTTON_2, FG_BUTTON_2), ('*', 2, 3, BG_BUTTON_1, FG_BUTTON_1),

            ('1', 3, 0, BG_BUTTON_2, FG_BUTTON_2), ('2', 3, 1, BG_BUTTON_2, FG_BUTTON_2),
            ('3', 3, 2, BG_BUTTON_2, FG_BUTTON_2), ('-', 3, 3, BG_BUTTON_1, FG_BUTTON_1),

            ('0', 4, 0, BG_BUTTON_2, FG_BUTTON_2), ('.', 4, 1, BG_BUTTON_2, FG_BUTTON_2),
            ('=', 4, 2, BG_BUTTON_1, FG_BUTTON_1), ('+', 4, 3, BG_BUTTON_1, FG_BUTTON_1),

            ('C', 5, 0, BG_BUTTON_1, FG_BUTTON_1), ('Exit', 5, 3, "red", FG_BUTTON_1)
        ]

        for (text, row, col, bg_color, fg_color) in buttons:
            self.create_button(text, row, col, bg_color, fg_color)

    def create_button(self, text, row, col, bg_color, fg_color):
        action_command = lambda: self.button_click(text)

        btn = tk.Button(
            self.frame,
            text=text,
            command=action_command,
            font=FONT_BOLD,
            fg=fg_color,
            bg=bg_color,
            padx=20,
            pady=10,
            relief=tk.RAISED
        )
        if text == '=' or text == 'C':
             btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="nsew")
        else:
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def button_click(self, char):
        if char == 'Exit':
            self.master.destroy()
        elif char == 'C':
            self.current_expression = ""
            self.input_text.set("0")
        elif char == '=':
            try:
                result = str(eval(self.current_expression))
                self.current_expression = result
                self.input_text.set(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.current_expression = ""
                self.input_text.set("Error")
        else:
            if self.current_expression == "0" or self.input_text.get() == "Error":
                 self.current_expression = ""

            self.current_expression += str(char)
            self.input_text.set(self.current_expression)


if __name__ == "_main_":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
