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
from interfaces import Repairable
from MusicalInstrument import MusicalInstrument

class StringFamily(MusicalInstrument, Repairable):
    def __init__(self, num_of_strings):
        self.num_of_strings = num_of_strings
        
    def get_num_of_strings(self):
        return self.num_of_strings