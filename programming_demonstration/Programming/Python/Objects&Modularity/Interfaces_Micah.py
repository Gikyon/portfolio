""""
Assignment #: 1
o Course: PROG23199
o Your full name: Micah Joshua Rahardjo
o Your Sheridan Student Number: 991687206
o Instructor’s name: Syed Tanbeer
"""

from abc import ABC, abstractmethod

class musical_instrument(ABC): #for abstract method of make sound

    def __init__(self):
        pass

    @abstractmethod
    def make_sound():
        pass

class playable(ABC): #for abstract playable method
    def __init__(self):
        pass

    @abstractmethod
    def how_to_play():
        pass

class priceProvider(ABC): #for abstract price method

    def __init__(self):
        pass

    @abstractmethod
    def price_provider():
        pass

class repairable(ABC): #for abstract repairable method
    def __init__(self):
        pass

    @abstractmethod
    def how_to_repair():
        pass