# Assignment #: 01
# Course: PROG23199
# Developer Name: Nicholas McClure
# Student ID #: 991693366
# Due Date: 2025/02/02
# Instructor's Name: Syed Tanbeer

# My Site: https://n-mcclure.github.io/
# My GitHub: https://github.com/N-McClure
# My LinkedIn: https://www.linkedin.com/in/nick-mcclure-578565295/


# Imported Libraries and Modules:
from abc import ABC, abstractmethod
from interfaces import Repairbale, Colourable

# Instrument Class:
class MusicalInstrument(Repairbale, Colourable, ABC):
    # Method to Get Name:
    def get_name(self):
        pass
    
    # Method to Get Price:
    def get_price(self):
        pass
    
    # Method to shdoe playing instructions:
    def play_instructions(self):
        pass
    
    # Method to "make" a sound:
    def make_sound(self):
        pass

    
    
 