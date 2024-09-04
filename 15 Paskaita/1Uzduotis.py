import pygame
import numpy


import random


names = ["Jonas", "Skaiste", "Lina", "Petras", "Markas", "Egle", "Milda", "Loreta", "Rasa", "Kajus"]



for i in range(5):
    name = random.choice(names)
    print(name)
    names.remove(name)


