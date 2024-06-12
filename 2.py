import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry_operand1.get()) + float(entry_operand2.get())
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_operator.delete(0, tk.END)
        entry_operator.insert(0, '+')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry_operand1.get()) - float(entry_operand2.get())
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_operator.delete(0, tk.END)
        entry_operator.insert(0, '-')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def multiply():
    try:
        result = float(entry_operand1.get()) * float(entry_operand2.get())
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_operator.delete(0, tk.END)
        entry_operator.insert(0, '*')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def divide():
    try:
        operand2 = float(entry_operand2.get())
        if operand2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
            return
        result = float(entry_operand1.get()) / operand2
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_operator.delete(0, tk.END)
        entry_operator.insert(0, '/')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def power():
    try:
        result = float(entry_operand1.get()) ** float(entry_operand2.get())
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_operator.delete(0, tk.END)
        entry_operator.insert(0, '^')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def mod():
    try:
        result = float(entry_operand1.get()) % float(entry_operand2.get())
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_operator.delete(0, tk.END)
        entry_operator.insert(0, 'Mod')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def clear():
    entry_operand1.delete(0, tk.END)
    entry_operand2.delete(0, tk.END)
    entry_result.delete(0, tk.END)
    entry_operator.delete(0, tk.END)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Simple Calculator")

# Main frame for layout
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# Title label
title_label = tk.Label(main_frame, text="Simple Calculator", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Operators frame
frame_operators = tk.LabelFrame(main_frame, text="Operators", padx=10, pady=10)
frame_operators.grid(row=1, column=0, padx=10, pady=10)

button_add = tk.Button(frame_operators, text="+", width=5, command=add)
button_add.grid(row=0, column=0, padx=5, pady=5)

button_subtract = tk.Button(frame_operators, text="-", width=5, command=subtract)
button_subtract.grid(row=0, column=1, padx=5, pady=5)

button_multiply = tk.Button(frame_operators, text="*", width=5, command=multiply)
button_multiply.grid(row=1, column=0, padx=5, pady=5)

button_divide = tk.Button(frame_operators, text="/", width=5, command=divide)
button_divide.grid(row=1, column=1, padx=5, pady=5)

button_power = tk.Button(frame_operators, text="^", width=5, command=power)
button_power.grid(row=2, column=0, padx=5, pady=5)

button_mod = tk.Button(frame_operators, text="Mod", width=5, command=mod)
button_mod.grid(row=2, column=1, padx=5, pady=5)

# Operation frame
frame_operation = tk.LabelFrame(main_frame, text="Operation", padx=10, pady=10)
frame_operation.grid(row=1, column=1, padx=10, pady=10)

label_operand1 = tk.Label(frame_operation, text="Operand 1:")
label_operand1.grid(row=0, column=0, sticky=tk.E)

entry_operand1 = tk.Entry(frame_operation)
entry_operand1.grid(row=0, column=1, padx=5, pady=5)


entry_operator = tk.Entry(frame_operation, width=7, state="readonly")
entry_operator.grid(row=1, column=1, padx=5, pady=5)

label_operand2 = tk.Label(frame_operation, text="Operand 2:")
label_operand2.grid(row=2, column=0, sticky=tk.E)

entry_operand2 = tk.Entry(frame_operation)
entry_operand2.grid(row=2, column=1, padx=5, pady=5)

label_result = tk.Label(frame_operation, text="Result:")
label_result.grid(row=3, column=0, sticky=tk.E)

entry_result = tk.Entry(frame_operation)
entry_result.grid(row=3, column=1, padx=5, pady=5)

button_clear = tk.Button(frame_operation, text="Clear", command=clear)
button_clear.grid(row=4, column=0, padx=5, pady=5)

button_exit = tk.Button(frame_operation, text="Exit", command=exit_app)
button_exit.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
