import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Get the operands from the entry widgets
        operand1 = float(entry1.get())
        operand2 = float(entry2.get())
        
        # Get the operator from the selected button
        operator = operator_var.get()
        
        # Perform the calculation based on the operator
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            result = operand1 / operand2
        elif operator == '\\':
            result = operand1 // operand2
        elif operator == '^':
            result = operand1 ** operand2
        elif operator == 'Mod':
            result = operand1 % operand2
        else:
            raise ValueError("Invalid operator")

        # Display the result
        result_label.config(text=f"Result: {result}")
    except ValueError:
        # If the input is invalid, show an error message
        messagebox.showerror("Invalid input", "Please enter valid numbers and select an operator")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result:")

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
tk.Label(root, text="Operand 1:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

operator_var = tk.StringVar(value='+')
tk.Label(root, text="Operator:").grid(row=1, column=0)
operator_label = tk.Label(root, textvariable=operator_var)
operator_label.grid(row=1, column=1)

tk.Label(root, text="Operand 2:").grid(row=2, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, columnspan=2)

# Create operator buttons
operators = ['+', '-', '*', '/', '\\', '^', 'Mod']
for i, op in enumerate(operators):
    tk.Radiobutton(root, text=op, variable=operator_var, value=op).grid(row=4, column=i)

# Create calculate, clear, and exit buttons
tk.Button(root, text="Calculate", command=calculate).grid(row=5, column=0)
tk.Button(root, text="Clear", command=clear).grid(row=5, column=1)
tk.Button(root, text="Exit", command=exit_app).grid(row=5, column=2)

# Run the Tkinter event loop
root.mainloop()
