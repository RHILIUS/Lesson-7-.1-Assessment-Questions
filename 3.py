import tkinter as tk
from tkinter import messagebox

def calculate_total():
    try:
        # Get the selected bagel price
        bagel_price = 0
        if bagel_var.get() == "White":
            bagel_price = 1.25
        elif bagel_var.get() == "Whole Wheat":
            bagel_price = 1.50

        # Get the selected toppings prices
        toppings_price = 0
        if cream_cheese_var.get():
            toppings_price += 0.50
        if butter_var.get():
            toppings_price += 0.25
        if blueberry_jam_var.get():
            toppings_price += 0.75
        if raspberry_jam_var.get():
            toppings_price += 0.75
        if peach_jelly_var.get():
            toppings_price += 0.75

        # Get the selected coffee price
        coffee_price = 0
        if coffee_var.get() == "Regular Coffee":
            coffee_price = 1.25
        elif coffee_var.get() == "Cappuccino":
            coffee_price = 2.00
        elif coffee_var.get() == "Cafe au lait":
            coffee_price = 1.75

        # Calculate subtotal, tax, and total
        subtotal = bagel_price + toppings_price + coffee_price
        tax = subtotal * 0.07
        total = subtotal + tax

        # Display the prices
        subtotal_entry.delete(0, tk.END)
        subtotal_entry.insert(0, f"${subtotal:.2f}")
        tax_entry.delete(0, tk.END)
        tax_entry.insert(0, f"${tax:.2f}")
        total_entry.delete(0, tk.END)
        total_entry.insert(0, f"${total:.2f}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def reset_form():
    # Reset all the selections
    bagel_var.set("")
    cream_cheese_var.set(0)
    butter_var.set(0)
    blueberry_jam_var.set(0)
    raspberry_jam_var.set(0)
    peach_jelly_var.set(0)
    coffee_var.set("None")
    subtotal_entry.delete(0, tk.END)
    tax_entry.delete(0, tk.END)
    total_entry.delete(0, tk.END)

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Brandi's Bagel House")

# Create the heading
heading_label = tk.Label(root, text="Brandi's Bagel House", font=("Arial", 24))
heading_label.grid(row=0, column=0, columnspan=4, pady=10)

# Bagel options
bagel_frame = tk.LabelFrame(root, text="Pick a Bagel", padx=10, pady=10)
bagel_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")
bagel_var = tk.StringVar()
tk.Radiobutton(bagel_frame, text="White ($1.25)", variable=bagel_var, value="White").pack(anchor='w')
tk.Radiobutton(bagel_frame, text="Whole Wheat ($1.50)", variable=bagel_var, value="Whole Wheat").pack(anchor='w')

# Toppings options
toppings_frame = tk.LabelFrame(root, text="Pick Your Toppings", padx=10, pady=10)
toppings_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")
cream_cheese_var = tk.IntVar()
butter_var = tk.IntVar()
blueberry_jam_var = tk.IntVar()
raspberry_jam_var = tk.IntVar()
peach_jelly_var = tk.IntVar()
tk.Checkbutton(toppings_frame, text="Cream Cheese ($.50)", variable=cream_cheese_var).pack(anchor='w')
tk.Checkbutton(toppings_frame, text="Butter ($.25)", variable=butter_var).pack(anchor='w')
tk.Checkbutton(toppings_frame, text="Blueberry Jam ($.75)", variable=blueberry_jam_var).pack(anchor='w')
tk.Checkbutton(toppings_frame, text="Raspberry Jam ($.75)", variable=raspberry_jam_var).pack(anchor='w')
tk.Checkbutton(toppings_frame, text="Peach Jelly ($.75)", variable=peach_jelly_var).pack(anchor='w')

# Coffee options
coffee_frame = tk.LabelFrame(root, text="Want Coffee with That?", padx=10, pady=10)
coffee_frame.grid(row=1, column=1, padx=10, pady=10, sticky="w")
coffee_var = tk.StringVar(value="None")
tk.Radiobutton(coffee_frame, text="None", variable=coffee_var, value="None").pack(anchor='w')
tk.Radiobutton(coffee_frame, text="Regular Coffee ($1.25)", variable=coffee_var, value="Regular Coffee").pack(anchor='w')
tk.Radiobutton(coffee_frame, text="Cappuccino ($2.00)", variable=coffee_var, value="Cappuccino").pack(anchor='w')
tk.Radiobutton(coffee_frame, text="Cafe au lait ($1.75)", variable=coffee_var, value="Cafe au lait").pack(anchor='w')

# Price display
price_frame = tk.LabelFrame(root, text="Price", padx=10, pady=10)
price_frame.grid(row=2, column=1, padx=10, pady=10, sticky="w")
tk.Label(price_frame, text="Subtotal:").grid(row=0, column=0, sticky="w")
subtotal_entry = tk.Entry(price_frame, width=10)
subtotal_entry.grid(row=0, column=1)
tk.Label(price_frame, text="Tax:").grid(row=1, column=0, sticky="w")
tax_entry = tk.Entry(price_frame, width=10)
tax_entry.grid(row=1, column=1)
tk.Label(price_frame, text="Total:").grid(row=2, column=0, sticky="w")
total_entry = tk.Entry(price_frame, width=10)
total_entry.grid(row=2, column=1)

# Buttons
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(button_frame, text="Calculate Total", command=calculate_total).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Reset Form", command=reset_form).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Exit", command=exit_app).grid(row=0, column=2, padx=5)

# Run the Tkinter event loop
root.mainloop()
