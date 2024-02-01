""""
Assignment #: 1
o Course: PROG23199
o Your full name: Micah Joshua Rahardjo
o Your Sheridan Student Number: 991687206
o Instructor’s name: Syed Tanbeer
"""

from Percussion_Micah import percussion
from String_Micah import string

class Piano(percussion,string): #a member of percussion family as well as the member of the string family

    def __init__(self, num_keys, num_strings, price = 725.00, play = "By hitting the keys that trigger hammers to hit the strings", repair = "replace the broken strings or keys", sound = "Vibrating soundboard", name = "piano"):
        super().__init__(num_keys, price, play, repair, sound)
        self.num_strings = num_strings
        self.name = name

    def special_features(self): #piano features
        return print (f"number of keys for piano = {self.num_keys}\nnumber of the strings for piano = {self.num_strings}")
        
    def output(self): #piano details
        print ("---------------------Piano----------------------")
        print(self.make_sound())
        print (self.how_to_play())
        print (self.how_to_repair())
        print (self.price_provider())