""""
Assignment #: 1
o Course: PROG23199
o Your full name: Micah Joshua Rahardjo
o Your Sheridan Student Number: 991687206
o Instructor’s name: Syed Tanbeer
"""

from Interfaces_Micah import musical_instrument, playable, priceProvider, repairable

class percussion(musical_instrument, playable, priceProvider, repairable): #percussion family is an instrument, playable, has a price, and repairable

    def __init__(self, num_keys, price, play, repair, sound):
    
        self.num_keys = num_keys
        self.price = price
        self.play = play
        self.repair = repair
        self.sound = sound

    def make_sound(self):  
        return f"make sound = {self.sound}"

    def how_to_play(self):
        return f"how to play = {self.play}"

    def price_provider(self):
        return f"price = $ {self.price}"

    def how_to_repair(self):
        return f"how to repair = {self.repair}"
        
    def output(self): #every percussion details blueprint
        print(self.make_sound())
        print (self.how_to_play())
        print (self.how_to_repair())
        print (self.price_provider())

class Drum(percussion): #a member of the percussion family

    def __init__(self, num_keys, diameter, price = 349.50, play = "By hitting the membrane with sticks", repair = "replace the membrane", sound = "Vibrating stretched membrane", name = "drum"):
        super().__init__(num_keys, price, play, repair, sound)
        self.diameter = diameter
        self.name = name

    def special_features(self): #drum features
        return print (f"number of keys for drum = {self.num_keys}\nsize of the diameter for drum = {self.diameter}")
        
    def output(self): #drum details
        print ("---------------------Drum----------------------")
        print(self.make_sound())
        print (self.how_to_play())
        print (self.how_to_repair())
        print (self.price_provider())

class Xylophone(percussion): #a member of the percussion family

    def __init__(self, num_keys, price = 49.00, play = "By hitting the bars with two mallets", repair = "replace the broken keys", sound = "Through resonator", name = "xylophone"):
        super().__init__(num_keys, price, play, repair, sound)
        self.name = name

    def special_features(self): #xylophone features
        return print (f"number of keys for xylophone = {self.num_keys}")
        
    def output(self): #xylophone details
        print ("---------------------Xylophone----------------------")
        print(self.make_sound())
        print (self.how_to_play())
        print (self.how_to_repair())
        print (self.price_provider())
