from breezypythongui import EasyFrame

class PizzaBuilder(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Radio Button Demo")

        self.addLabel(text="Meat", row=0, column=0)
        self.meatGroup = self.addRadiobuttonGroup(row=1,
                                                  column=0,
                                                  rowspan=2)
        defaultRB = self.meatGroup.addRadiobutton(text="chicken")
        self.meatGroup.setSelectedButton(defaultRB)
        self.meatGroup.addRadiobutton(text="Beef")

        self.addLabel(text="Potato",row=0, column=1)

        self.taterGroup = self.addRadiobuttonGroup(row=1,
                                                   column=1,
                                                   columnspan=2)
        defaultRB = self.taterGroup.addRadiobutton(text="French fries")
        self.taterGroup.setSelectedButton(defaultRB)
        self.taterGroup.addRadiobutton(text="Baked Potato")

def main():
    PizzaBuilder().mainloop()

if __name__ == "__main__":
    main()
