"""
File: Foster_FinalProject.py
Author: J. Mitchell Foster
This program allows a user to select toppings for a pizza and returns the toppings in a concise list.
"""
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Pizza Builder')
root.iconbitmap('images/slice_of_pizza.ico')

# Two images linked to specific variables
pizza_img = ImageTk.PhotoImage(Image.open("images/pizza.png"))
pizza_add = ImageTk.PhotoImage(Image.open("images/pizza_add.png"))

# Creates different frames in the program to isolate different ingredients.
crust_frame = LabelFrame(root, text="Crust Size", padx=10, pady=10)
crust_frame.grid(row=0, column=0)

sauce_frame = LabelFrame(root, text="Sauces", padx=10, pady=10)
sauce_frame.grid(row=0, column=1)

cheese_frame = LabelFrame(root, text="Cheese", padx=10, pady=10)
cheese_frame.grid(row=0, column=2)
cheese_label = Label(cheese_frame, text="Cheese is default")
cheese_label.pack()

meat_frame = LabelFrame(root, text="Meats", padx=10, pady=10)
meat_frame.grid(row=0, column=3)

veggie_frame = LabelFrame(root, text="Vegetables", padx=10, pady=10)
veggie_frame.grid(row=0, column=4)

# List of different Crusts
CRUSTS = {
    "Little Zip": 6.95,
    "Big Zip": 8.70,
    "Cauliflower": 12.15,
    "Gluten Free": 10.25,
    "Zero Carb": 11.45
}
# List of different meats
MEATS = {
    "Pepperoni": .75,
    "Sausage": .75,
    "Chicken": .75,
    "Meatball": .75,
    "Pork": .75,
    "Bacon": .75,
    "No Meat": .75

}

pizza_crust = StringVar()
pizza_crust.set("Little Zip")

# Populates the crust selection
for text, price in CRUSTS.items():
    Radiobutton(crust_frame, text=f"{text} ${price:.2f}", variable=pizza_crust, value=text).pack()

# populates the sauce selection
sb1_var = IntVar()
sb2_var = IntVar()
sb3_var = IntVar()
sb4_var = IntVar()
sb5_var = IntVar()
sb6_var = IntVar()

sb1 = Checkbutton(sauce_frame, text="Red Sauce", variable=sb1_var, onvalue=1, offvalue=0)
sb2 = Checkbutton(sauce_frame, text="Pesto", variable=sb2_var, onvalue=1, offvalue=0)
sb3 = Checkbutton(sauce_frame, text="Garlic Butter", variable=sb3_var, onvalue=1, offvalue=0)
sb4 = Checkbutton(sauce_frame, text="BBQ", variable=sb4_var, onvalue=1, offvalue=0)
sb5 = Checkbutton(sauce_frame, text="Buffalo", variable=sb5_var, onvalue=1, offvalue=0)
sb6 = Checkbutton(sauce_frame, text="Ranch", variable=sb6_var, onvalue=1, offvalue=0)

sb1.pack()
sb2.pack()
sb3.pack()
sb4.pack()
sb5.pack()
sb6.pack()

# populates the cheese selection
cb1_var = IntVar()
cb2_var = IntVar()
cb1 = Checkbutton(cheese_frame, text="No Cheese", variable=cb1_var, onvalue=1, offvalue=0)
cb2 = Checkbutton(cheese_frame, text="Dairy-Free Cheese", variable=cb2_var, onvalue=1, offvalue=0)
cb1.pack()
cb2.pack()

# populates the Meat Selection
meat_var = StringVar()
meat_var.set("Pepperoni")
for text, price in MEATS.items():
    Radiobutton(meat_frame, text=f"{text} ${price:.2f}", variable=meat_var, value=text).pack()

# populates the Veggie Selection
veg1_var = IntVar()
veg2_var = IntVar()
veg3_var = IntVar()
veg4_var = IntVar()
veg5_var = IntVar()
veg6_var = IntVar()
veg7_var = IntVar()
veg8_var = IntVar()

veg1 = Checkbutton(veggie_frame, text="Mushroom", variable=veg1_var, onvalue=1, offvalue=0)
veg2 = Checkbutton(veggie_frame, text="Olives", variable=veg2_var, onvalue=1, offvalue=0)
veg3 = Checkbutton(veggie_frame, text="Green Pepper", variable=veg3_var, onvalue=1, offvalue=0)
veg4 = Checkbutton(veggie_frame, text="Banana Pepper", variable=veg4_var, onvalue=1, offvalue=0)
veg5 = Checkbutton(veggie_frame, text="Tomato", variable=veg5_var, onvalue=1, offvalue=0)
veg6 = Checkbutton(veggie_frame, text="Garlic Cloves", variable=veg6_var, onvalue=1, offvalue=0)
veg7 = Checkbutton(veggie_frame, text="Spinach", variable=veg7_var, onvalue=1, offvalue=0)
veg8 = Checkbutton(veggie_frame, text="Onion", variable=veg8_var, onvalue=1, offvalue=0)

veg1.pack()
veg2.pack()
veg3.pack()
veg4.pack()
veg5.pack()
veg6.pack()
veg7.pack()
veg8.pack()


# All the checks that happen when the finished button is clicked

def clicked():
    final_items = []

    if sb1_var.get():
        final_items.append("Red Sauce")
    if sb2_var.get():
        final_items.append("Pesto")
    if sb3_var.get():
        final_items.append("Garlic Butter")
    if sb4_var.get():
        final_items.append("BBQ")
    if sb5_var.get():
        final_items.append("Buffalo")
    if sb6_var.get():
        final_items.append("Ranch")
    if cb1_var.get():
        final_items.append("No Cheese")
    if cb2_var.get():
        final_items.append("Dairy-Free Cheese")

    if veg1_var.get():
        final_items.append("Mushroom")
    if veg2_var.get():
        final_items.append("Olives")
    if veg3_var.get():
        final_items.append("Green Pepper")
    if veg4_var.get():
        final_items.append("Banana Pepper")
    if veg5_var.get():
        final_items.append("Tomato")
    if veg6_var.get():
        final_items.append("Garlic Cloves")
    if veg7_var.get():
        final_items.append("Spinach")
    if veg8_var.get():
        final_items.append("Onion")
    results = ""
    total = 0
    total += CRUSTS[pizza_crust.get()]
    total += MEATS[meat_var.get()]
    results += pizza_crust.get() + '\n'
    results += meat_var.get()+ '\n'
    for item in final_items:
        results += f'{item} \n'
    results += f'\n Total: ${total:.2f}'
    messagebox.showinfo("Finished Pizza", results)


# Builds the buttons to exit and build the pizza
nextButton = Button(root, command=clicked, image=pizza_add)
nextButton.grid(row=6, column=0, columnspan=2, rowspan=3)
button_quit = Button(root, text="Exit", command=root.quit, width=10, height=4)
button_quit.grid(row=6, column=3, rowspan=3)

root.mainloop()
