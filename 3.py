import tkinter as tk
from tkinter import font
from tkinter import messagebox

# ===== DEF =====
# Calculate the bagel
def calculateTotal():
    try:
        
        # BAGEL
        bagel_price = 0
        if bagel_choice.get() == "White":
            bagel_price = 1.25
        elif bagel_choice.get() == "Whole Wheat":
            bagel_price = 1.50

        # TOPPINGS
        toppings_price = 0
        if var.get():
            toppings_price += 0.50
        if var1.get():
            toppings_price += 0.25
        if var2.get():
            toppings_price += 0.75
        if var3.get():
            toppings_price += 0.75
        if var4.get():
            toppings_price += 0.75

        # COFFEE
        coffee_price = 0
        if coffee_choice.get() == "Regular Coffee":
            coffee_price = 1.25
        elif coffee_choice.get() == "Cappuccino":
            coffee_price = 2.00
        elif coffee_choice.get() == "Cafe au lait":
            coffee_price = 1.75

        # TOTAL
        subtotal = bagel_price + toppings_price + coffee_price
        tax = subtotal * 0.07
        total = subtotal + tax

        # DISPLAY
        subTotal_entry.delete(0, tk.END)
        subTotal_entry.insert(0, f"${subtotal:.2f}")
        tax_entry.delete(0, tk.END)
        tax_entry.insert(0, f"${tax:.2f}")
        total_entry.delete(0, tk.END)
        total_entry.insert(0, f"${total:.2f}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def formReset():
    bagel_choice.set("")
    var.set(0)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    coffee_choice.set("None")
    subTotal_entry.delete(0, tk.END)
    tax_entry.delete(0, tk.END)
    total_entry.delete(0, tk.END)

def exit():
    root.destroy()

# WINDOWS
root = tk.Tk()
root.title("Bagel and Coffee Price Calculator")

# TITLE
style = font.Font(family="Times New Roman", size=20, slant="italic", weight="bold")
label = tk.Label(
    root,
    text="Brandi's Bagel House",
    font=style
)
label.pack(pady=20)

# ===== MAIN CONTAINER FRAME =======
mainframe = tk.Frame(root)
mainframe.pack()  # pady = 10

# ===== LEFT FRAME =======
leftframe = tk.Frame(mainframe)
leftframe.grid(row=0, column=0, padx=20, sticky='n')

# child of leftframe
leftframe1 = tk.LabelFrame(leftframe)
leftframe1.grid(row=0, column=0, pady=5)

# widgets of leftframe1
label_left = tk.Label(
    leftframe1,
    text="Pick a Bagel"
)
label_left.grid(sticky='w', pady=(0, 10))

# Choices
bagel_choice = tk.StringVar(value="White")

radio = tk.Radiobutton(
    leftframe1,
    text="White ($1.25)",
    value="White",
    variable=bagel_choice
)
radio.grid(sticky='w')

radio1 = tk.Radiobutton(
    leftframe1,
    text="Whole Wheat ($1.50)",
    value="Whole Wheat",
    variable=bagel_choice
)
radio1.grid(sticky='w', padx=(0, 30))

# child of leftframe
leftframe2 = tk.LabelFrame(leftframe)
leftframe2.grid(row=1, column=0, pady=25)  # i add 25 padding here

# widgets of leftframe2
label1_left = tk.Label(
    leftframe2,
    text="Pick Your Toppings"
)
label1_left.grid(sticky='w', pady=(0, 10))

# Choices
var = tk.IntVar()

toppings = tk.Checkbutton(
    leftframe2,
    text="Cream Cheese ($.50)",
    variable=var
)
toppings.grid(sticky='w', padx=(0, 30))

var1 = tk.IntVar()
toppings_1 = tk.Checkbutton(
    leftframe2,
    text="Butter ($.25)",
    variable=var1
)
toppings_1.grid(sticky='w')

var2 = tk.IntVar()
toppings_2 = tk.Checkbutton(
    leftframe2,
    text="Blueberry Jam ($.75)",
    variable=var2
)
toppings_2.grid(sticky='w')

var3 = tk.IntVar()
toppings_3 = tk.Checkbutton(
    leftframe2,
    text="Raspberry Jam ($.75)",
    variable=var3
)
toppings_3.grid(sticky='w')

var4 = tk.IntVar()
toppings_4 = tk.Checkbutton(
    leftframe2,
    text="Peach Jelly ($.75)",
    variable=var4
)
toppings_4.grid(sticky='w')

# ===== RIGHT FRAME =======

rightframe = tk.Frame(mainframe)
rightframe.grid(row=0, column=1, padx=20, sticky='n')

# child of rightframe
rightframe1 = tk.LabelFrame(rightframe)
rightframe1.grid(row=0, column=0, pady=5, sticky='w')

# widgets of rightframe1
label_right = tk.Label(
    rightframe1,
    text="Want Coffee with That?"
)
label_right.grid(sticky='w', pady=(0, 10))

# Choices
coffee_choice = tk.StringVar(value="None")

coffee = tk.Radiobutton(
    rightframe1,
    text="None",
    value="None",
    variable=coffee_choice
)
coffee.grid(sticky='w')

coffee_1 = tk.Radiobutton(
    rightframe1,
    text="Regular Coffee ($1.25)",
    value="Regular Coffee",
    variable=coffee_choice
)
coffee_1.grid(sticky='w', padx=(0, 30))

coffee_2 = tk.Radiobutton(
    rightframe1,
    text="Cappuccino ($2.00)",
    value="Cappuccino",
    variable=coffee_choice
)
coffee_2.grid(sticky='w')

coffee_3 = tk.Radiobutton(
    rightframe1,
    text="Cafe au lait ($1.75)",
    value="Cafe au lait",
    variable=coffee_choice
)
coffee_3.grid(sticky='w')

# child of rightframe
rightframe2 = tk.LabelFrame(rightframe)
rightframe2.grid(row=1, column=0, pady=20, sticky='w')


# widgets of rightframe2
label_right1 = tk.Label(
    rightframe2,
    text="Price"
)
label_right1.grid(sticky='w', padx=(0, 50))

# grandchild of rightframe
rf2 = tk.Frame(rightframe2)
rf2.grid(row=1, column=0, pady=5, sticky='w')

subTotal = tk.Label(
    rf2,
    text="Subtotal"
)
subTotal.grid(row=0, column=0, sticky='e')

subTotal_entry = tk.Entry(
    rf2
)
subTotal_entry.grid(row=0, column=1, padx=5, pady=3)

tax = tk.Label(
    rf2,
    text="Tax"
)
tax.grid(row=1, column=0, sticky='e')

tax_entry = tk.Entry(
    rf2
)
tax_entry.grid(row=1, column=1, padx=5,  pady=3)

total = tk.Label(
    rf2,
    text="Total"
)
total.grid(row=2, column=0, sticky='e')

total_entry = tk.Entry(
    rf2
)
total_entry.grid(row=2, column=1, padx= 5,  pady=3)


# ===== BOTTOM FRAME =======

button_frame = tk.Frame(mainframe)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(
  button_frame, text="Calculate Total", command=calculateTotal).grid(row=0, column=0, padx=10)

tk.Button(
  button_frame, text="Reset Form", command=formReset).grid(row=0, column=1, padx=10)

tk.Button(
  button_frame, text="Exit", command=exit).grid(row=0, column=2, padx=10)


# MAIN LOOP
root.mainloop()
