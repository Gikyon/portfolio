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
from OrderList_Micah import Order

if __name__ == "__main__":
    # All objects
    drum = Drum(0, 20)
    xylophone = Xylophone(25)
    piano = Piano(88, 230)
    harp = Harp(40)
    violin = Violin(4)
    flute = Flute()

    #all objects in a form of a list
    list_of_instruments = [drum, xylophone, piano, harp, violin, flute]

    output_num = 1 #output number control and this loop will show all the instruments detail
    for i in list_of_instruments:
        print (f"---------------------OUTPUT{output_num}-------------------")
        i.output()
        output_num += 1

    #print all instrument's special features
    print ("---------------------OUTPUT7----------------------")
    print ("---------------------SPECIAL FEATURE--------------")
    for i in list_of_instruments:
        i.special_features()

    print ("---------------------OUTPUT8----------------------")
    dicts = {} #dictionary with instrument's price as key and instrument's name as value
    for value in list_of_instruments:
        dicts[value.price] = value.name

    # sorts the dictionary by the key
    ordered_list = sorted(dicts.items())

    # prints the dictionary with an ascending order
    print ("[Instrument's price from low to high]")
    for i in ordered_list:
        print(f"{i[1]} : {i[0]}")

    print ("---------------------OUTPUT9----------------------")
    percussion_family = [drum, xylophone, piano] #specifying each group so it looks more neat
    string_family = [piano, harp, violin]
    woodwind_family = [flute]

    # Bob's order with student number 9 digits
    Bob = Order(111111111, "bob")
    for i in percussion_family:
        Bob.add_instrument(i)
    print (Bob.output())

    # Alice's order with student number 9 digits
    Alice = Order(222222222, "Alice")
    for i in string_family:
        Alice.add_instrument(i)
    print(Alice.output())

    # custom order
    print ("---------------------CUSTOM ORDER----------------------")
    control = 1
    while control != 0:
        print ("Please enter your order without space\nd = Drum, f = Flute, h = Harp, p = Piano, v = Violin, and x = Xylophone")
        micah = Order(991687206, "Micah")
        micah.new_order() #ask for the order and confirms it
        print (micah.output()) #printing the total
        print("---------------------------------------------------------------------------------")