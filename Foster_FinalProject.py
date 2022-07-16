#This application asks for the user to build a pizza and is given a confirmation and the price of
#All ingredients added to the pizza.

from tkinter import *

win = Tk() #creates the main window
win.title("Pizza Maker")

def check():
    string=''
    if(cb_var1.get()):
        string += "Little Zip\t"
    if (cb_var2.get()):
        string += "Big Zip\t"
    if (cb_var3.get()):
        string += "Gluten Free\t"
    if (cb_var4.get()):
        string += "Cauliflower\t"
    if (cb_var5.get()):
        string += "ZeroCarb Chicken\t"
    txt.insert(1.0,string)

cb_var1 = IntVar()
cb1 = Checkbutton(win, text='Little Zip', variable=cb_var1, onvalue=1, offvalue=0, height=5, width=20)#.grid(row=0, sticky=W)

cb_var2 = IntVar()
cb2 = Checkbutton(win, text='Big Zip', variable=cb_var2, onvalue=1, offvalue=0, height=5, width=20)#.grid(row=1, sticky=W)

cb_var3 = IntVar()
cb3 = Checkbutton(win, text='Gluten Free', variable=cb_var3, onvalue=1, offvalue=0, height=5, width=20)#.grid(row=2, sticky=W)

cb_var4 = IntVar()
cb4 = Checkbutton(win, text="Cauliflower", variable=cb_var4,onvalue=1, offvalue= 0, height=5, width=20)#.grid(row=3, sticky=W)

cb_var5 =IntVar()
cb5 = Checkbutton(win, text="ZeroCarb Chicken", variable=cb_var5,onvalue=1, offvalue= 0, height=5, width=20)#.grid(row=4, sticky=W)

txt=Text(win,height=3,width=20)
btn = Button(win,text="Done",command=check)

cb1.pack()
cb2.pack()
cb3.pack()
cb4.pack()
txt.pack()
btn.pack()
#basePizza = 6.95
#igPizza = basePizza + 1.75
#glutenPizza = basePizza + 3.30
#cauliPizza = basePizza + 5.20
#zeroCarbPizza = basePizza + 4.50

win.mainloop()