""""
Assignment #: 1
o Course: PROG23199
o Your full name: Micah Joshua Rahardjo
o Your Sheridan Student Number: 991687206
o Instructor’s name: Syed Tanbeer
"""
from Interfaces_Micah import musical_instrument, playable, priceProvider

class woodwind(musical_instrument, playable, priceProvider): #woodwind family is an instrument, playable, has a price, but not repairable

    def __init__(self, price, play, sound):
        
        self.price = price
        self.play = play
        self.sound = sound

    def make_sound(self):  
        return f"make sound = {self.sound}"

    def how_to_play(self):
        return f"how to play = {self.play}"

    def price_provider(self):
        return f"price = $ {self.price}"

    def special_features(self):
        return print (f"made out of wood")
        
    def output(self): #blueprint for the details of the woodwind family
        print(self.make_sound())
        print (self.how_to_play())
        print (self.price_provider())

class Flute(woodwind): #flute is a member of the woodwind family

    def __init__(self, price = 74.99, play = "By blowing in to the flute", sound = "Guiding a stream of air", name = "flute"):
        super().__init__(price, play, sound)
        self.name = name

    def special_features(self): #special features of flute
        return print (f"made out of wood")
        
    def output(self): #details of flute
        print ("---------------------Flute----------------------")
        print(self.make_sound())
        print (self.how_to_play())
        print (self.price_provider())

flute = Flute()

print (flute.special_features())