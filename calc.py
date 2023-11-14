import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, master):
        # Window Initialization
        self.master = master
        self.master.title("DJM Calculator")

        # Entry Widget for Displaying Input and Results
        self.entry_var = tk.StringVar()
        entry = ttk.Entry(master, textvariable=self.entry_var, font=('Arial', 14), justify='right', state='disabled')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Buttons for Numbers and Basic Operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+', 'π' 
        ]

        # Set Up Grid for Buttons
        row_val, col_val = 1, 0
        for button in buttons:
            # Button Creation and Grid Placement
            ttk.Button(master, text=button, command=lambda b=button: self.mouse(b)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure Row and Column Weights for Proportional Expansion
        for i in range(1, 5):
            master.columnconfigure(i, weight=1)
            master.rowconfigure(i, weight=1)

        # Bind Keyboard Events to the on_key_press Function
        master.bind('<Key>', self.on_key_press)

    def mouse(self, button):
        # Button Click Handling (Mouse Events)
        current_entry = self.entry_var.get()

        if button == '=':
            try:
                # Evaluate Expression and Display Result
                result = eval(current_entry)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")
        elif button == 'π':
            # Append the Value of pi to the Current Entry
            self.entry_var.set(current_entry + str(math.pi))
        else:
            # Append Clicked Button's Value to Current Entry
            self.entry_var.set(current_entry + button)

    def on_key_press(self, event):
        # Key Press Handling
        key = event.char
        if key.isdigit() or key in ['+', '-', '*', '/', '.']:
            # Simulate Button Click for Digits, Operators, or Decimal Point
            self.mouse(key)
        elif key == '\r':
            # Simulate Button Click for 'Enter'
            self.mouse('=')
        elif key == '\x08':
            # Remove Last Character from Entry for 'Backspace'
            current_entry = self.entry_var.get()
            self.entry_var.set(current_entry[:-1])
        elif key == '\x7F':
            # Clear Entire Entry for 'Delete'
            self.entry_var.set("")

def main():
    # Main Function
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    # Main Execution Block
    main()
