import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        # Get the integer from the entry widget
        N = int(entry.get())
        
        # Calculate the sum
        total_sum = sum(range(1, N + 1))
        
        # Display the result
        result_label.config(text=f"The sum of 1 + 2 + ... + {N} is: {total_sum}")
    except ValueError:
        # If the input is not an integer, show an error message
        messagebox.showerror("Invalid input", "Please enter a valid integer")

# Create the main window
root = tk.Tk()
root.title("Sum Calculator")

# Create and place the widgets
prompt_label = tk.Label(root, text="Enter an integer:")
prompt_label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Calculate Sum", command=calculate_sum)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()