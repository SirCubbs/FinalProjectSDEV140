from breezypythongui import *

class PizzaBuilder(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self)

        # Pizza Labels
        self.label = self.addLabel(text="Size",row=0,column=0)
        self.pizzaGroup = self.addRadiobuttonGroup(row=1, column=0, rowspan=6)
        defaultRB = self.pizzaGroup.addRadiobutton(text="Little Zip")
        self.pizzaGroup.setSelectedButton(defaultRB)
        self.pizzaGroup.addRadiobutton(text="Big Zip")
        self.pizzaGroup.addRadiobutton(text="Cauliflower Crust")
        self.pizzaGroup.addRadiobutton(text="ZeroCarb Crust")
        self.pizzaGroup.addRadiobutton(text="Gluten Free (Allergy)")
        self.pizzaGroup.addRadiobutton(text="Gluten Free (Preference)")

        # Sauce Labels
        self.addLabel(Text="Sauces",row=0,column=1)
        self.redSauce = self.addCheckbutton(Text="Italian Red",row=1,column=1)
        self.pesto = self.addCheckbutton(Text="Azzip Pesto",row=2,column=1)
        self.garButter = self.addCheckbutton(Text="Garlic Butter",row=3,column=1)
        self.ranch = self.addCheckbutton(Text="House Ranch",row=4,column=1)
        self.buffalo = self.addCheckbutton(Text="Buffalo",row=5,column=1)
        self.bbq = self.addCheckbutton(Text="BBQ Sauce",row=6,column=1)
        self.noSauce = self.addCheckbutton(Text="No Sauce",row=7,column=1)

        # Cheese
        self.addLabel(Text="Cheese",row=0,column=2)
        self.noCheese = self.addCheckbutton(Text="No Cheese",row=1,column=2)
        self.mozz = self.addCheckbutton(Text="Mozzarella",row=2,column=2)
        self.dairyFree = self.addCheckbutton(Text="Dairy-Free Cheese",row=3,column=2)
        self.extraMozz = self.addCheckbutton(Text="Extra Mozzarella",row=4,column=2)

        # Meats
        self.addLabel(Text="Meat",row=0,column=3)
        self.meatGroup = self.addRadiobuttonGroup(row=1, column=3, rowspan=2)
        defaultMeat = self.meatGroup.addRadiobutton(Text="No Meat")
        self.meatGroup.setSelectedButton(defaultMeat)
        self.meatGroup.addRadiobutton(Text="Old World Pepperoni")
        self.meatGroup.addRadiobutton(Text="Italian Sausage")
        self.meatGroup.addRadiobutton(Text="Roasted Chicken")
        self.meatGroup.addRadiobutton(Text="Nueske's Bacon")
        self.meatGroup.addRadiobutton(Text="All Beef Meatball")
        self.meatGroup.addRadiobutton(Text="Smoked Pork")
        self.meatGroup.addRadiobutton(Text="Zero Sausage (V)")
        self.meatGroup.addRadiobutton(Text="Plant Based Pepperoni (V)")

        # Veggies
        self.addLabel(Text="Veggies",row=0,column=4)
        self.spinach = self.addCheckbutton(Text="Baby Spinach",row=1,column=4)
        self.mushroom = self.addCheckbutton(Text="Baby Portobello Mushrooms",row=2,column=4)
        self.grPepper = self.addCheckbutton(Text="Green Peppers",row=3,column=4)
        self.redOnion = self.addCheckbutton(Text="Red Onions",row=4,column=4)
        self.pineapple = self.addCheckbutton(Text="Pineapple",row=5,column=4)
        self.olives = self.addCheckbutton(Text="Artisan Olives",row=6,column=4)
        self.garlic = self.addCheckbutton(Text="Roasted Garlic",row=7,column=4)
        self.sdTomatoes = self.addCheckbutton(Text="Sun-Dried Tomatoes",row=8,column=4)
        self.bnaPepper = self.addCheckbutton(Text="Banana Pepper Rings",row=9,column=4)
        self.romaTomatoes = self.addCheckbutton(Text="Roma Tomatoes",row=10,column=4)
        self.potatoes = self.addCheckbutton(Text="Roasted Potatoes",row=11,column=4)
        self.hotPepper = self.addCheckbutton(Text="Hot Pepper Blend",row=12,column=4)
        self.cheeseBlend = self.addCheckbutton(Text="3-Cheese Blend on Top",row=13,column=4)

        self.addButton(Text="Build Pizza",row=14,column=0,
                       columnspan=3,command=self.buildPizza)

    def buildPizza(self):
        """Displays a message box with the pizza ingredients inside"""
        message = ""
        message += self.pizzaGroup.getSelectedButton()["text"] + "\n\n"
        if self.redSauce.isChecked():
            message += "Red Sauce\n\n"
        if self.pesto.isChecked():
            message += "Pesto\n\n"
        if self.garButter.isChecked():
            message += "Garlic Butter\n\n"
        if self.ranch.isChecked():
            message += "Ranch\n\n"
        if self.buffalo.isChecked():
            message += "Buffalo\n\n"
        if self.bbq.isChecked():
            message += "BBQ\n\n"
        if self.noSauce.isChecked():
            message += "No Sauce\n\n"
        message += self.meatGroup.getSelectedButton()["text"]+"\n\n"
        if self.spinach.isChecked():
            message += "Spinach\n\n"
        if self.mushroom.isChecked():
            message += "Mushroom\n\n"
        if self.grPepper.isChecked():
            message += "Green Pepper\n\n"
        if self.redOnion.isChecked():
            message += "Onion\n\n"
        if self.pineapple.isChecked():
            message += "Pineapple\n\n"
        if self.olives.isChecked():
            message += "Olives\n\n"
        if self.garlic.isChecked():
            message += "Garlic\n\n"
        if self.sdTomatoes.isChecked():
            message += "Sun-Dried Tomatoes\n\n"
        if self.bnaPepper.isChecked():
            message += "Banana Pepper\n\n"
        if self.romaTomatoes.isChecked():
            message += "Roma Tomatoes\n\n"
        if self.potatoes.isChecked():
            message += "Potatoes\n\n"
        if self.hotPepper.isChecked():
            message += "Hot Pepper Blend\n\n"
        if self.cheeseBlend.isChecked():
            message += "3 Cheese Blend\n\n"
        self.messageBox(title="Customer Order", message=message)


def main():
    PizzaBuilder().mainloop()

if __name__ == "__main__":
    main()

