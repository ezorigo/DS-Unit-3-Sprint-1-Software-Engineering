"""
Ways to organize the vast quantities and variety of goods
Acme Corporation manages and sells
"""

import random


class Product:
    """
    inplace docstring
    """


    def __init__(self, name=str, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        steal = self.price/self.weight
        if steal < 0.5:
            message = "Not so stealable..."
        elif (steal >= 0.5) & (steal < 1.0):
            message = "Kinda stealable."
        else:
            message = "Very stealable!"
        return message
    
    def explode(self):
        explode = self.flammability * self.weight
        if explode < 10:
            message = "...fizzle."
        elif (explode >= 10) & (explode < 50):
            message = "...boom!"
        else:
            message = "...BABOOM!!"
        return message

class BoxingGlove(Product):
    """
    placeholder docstring
    """
    def __init__(self, name=str, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def explode(self):
        message = "...it's a glove."
        return message

    def punch(self):
        if self.weight < 5:
            message = "That tickles."
        elif (self.weight >=5) & (self.weight < 15):
            message = "Hey that hurt!"
        else:
            message = "OUCH!"
        return message
