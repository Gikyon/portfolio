""""
Assignment #: 1
o Course: PROG23199
o Your full name: Micah Joshua Rahardjo
o Your Sheridan Student Number: 991687206
o Instructor’s name: Syed Tanbeer
"""

from Interfaces_Micah import musical_instrument, playable, priceProvider, repairable

class string(musical_instrument, playable, priceProvider, repairable): #string family is an instrument, playable, has a price, and repairable

    def __init__(self, num_strings, price, play, repair, sound): 
        
        self.num_strings = num_strings
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
        
    def output(self): #every string details blueprint
        print(self.make_sound())
        print (self.how_to_play())
        print (self.how_to_repair())
        print (self.price_provider())

class Harp(string): #member of the string family

    def __init__(self, num_strings, price = 255.00, play = "By strumming the strings and peddling to adjust the string length", repair = "replace the broken string", sound = "Vibrating strings", name = "harp"):
        super().__init__(num_strings, price, play, repair, sound)
        self.name = name

    def special_features(self): # harp features
        return print (f"number of strings for harp = {self.num_strings}")
        
    def output(self): #details of harp family
        print ("---------------------Harp----------------------")
        print(self.make_sound())
        print (self.how_to_play())
        print (self.how_to_repair())
        print (self.price_provider())

class Violin(string): #member of the string family

    def __init__(self, num_strings, price = 350.00, play = "By resting the violin on shoulder, plucking the strings bow and picking notes with fingers", repair = "replace the broken bridge", sound = "Vibrating strings", name = "violin"):
        super().__init__(num_strings, price, play, repair, sound)
        self.name = name

    def special_features(self): #violin special feature
        return print (f"number of strings for violin = {self.num_strings}")
        
    def output(self): #details of violin string
        print ("---------------------Violin----------------------")
        print(self.make_sound())
        print (self.how_to_play())
        print (self.how_to_repair())
        print (self.price_provider())