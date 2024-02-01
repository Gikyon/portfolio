""""
Assignment #: 1
o Course: PROG23199
o Your full name: Micah Joshua Rahardjo
o Your Sheridan Student Number: 991687206
o Instructor’s name: Syed Tanbeer
"""
from Woodwind_Micah import woodwind, Flute
from String_Micah import string, Harp, Violin
from Percussion_Micah import percussion, Drum, Xylophone
from Piano_Micah import Piano

# Every instrument object
drum = Drum(0, 20) 
xylophone = Xylophone(25)
piano = Piano(88, 230)
harp = Harp(40)
violin = Violin(4)
flute = Flute()

#List of instrument
list_of_instruments = [drum, xylophone, piano, harp, violin, flute]

#orderList class
class Order():
    
    def __init__(self, o_id, customer_name, orders = []):
        self.o_id = f"{o_id}"
        self.customer_name = customer_name
        self.orders = orders

    def id(self): #accessor + taking only 3 digits of student id
        id = self.o_id[-3]+self.o_id[-2]+self.o_id[-1]
        return f"({id})"

    def edit_id(self): #mutator
        newid = input("Please enter your new id: ")
        self.o_id = newid

    def name(self): #accessor
        return f"{self.customer_name}"

    def edit_name(self): #mutator
        newname = input("please enter your correct name: ")
        self.customer_name = newname
        
    def order(self): #accessor
        if self.orders == []: #if the user didn't add any instrument it will show
            return f"{self.orders} , you haven't order any instrument"
        else:
            list_of_orders = []
            for o in self.orders:
                list_of_orders.append(o.name)
            return f"{self.name()} ordered: {list_of_orders}"
        
    def new_order(self): #function for the last output
        neworder = []
        new_order_name = []
        str_order = input("Please enter your order : ")
        ls_order = list(str_order)
        for i in ls_order: #loop for the letters
            if i == "d": #add the instrument to order if the user input the initial charachter
                neworder.append(drum)
                new_order_name.append(drum.name)
            elif i == "x":
                neworder.append(xylophone)
                new_order_name.append(xylophone.name)
            elif i == "p":
                neworder.append(piano)
                new_order_name.append(piano.name)
            elif i == "h":
                neworder.append(harp)
                new_order_name.append(harp.name)
            elif i == "v":
                neworder.append(violin)
                new_order_name.append(violin.name)
            elif i == "f":
                neworder.append(flute)
                new_order_name.append(flute.name)
            else:
                pass
        self.orders = neworder
        name_a = self.name()
        print (f"{name_a} ordered : {new_order_name}")

    def add_instrument(self, instrument): #function for adding instrument (can only add 1 at a time)
        self.orders.append(instrument)
        

    def output(self): #complete output for the order
        id_a = self.id()
        order_total = 0
        for p in self.orders:
            order_total += p.price

        return f"Order total for {self.customer_name} {id_a} : {order_total}"