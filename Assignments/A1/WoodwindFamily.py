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
from MusicalInstrument import MusicalInstrument

class WoodwindFamily(MusicalInstrument):
    def __init__(self, made_of):
        self.made_of = "Wood"
    
    def get_made_of(self):
        return self.made_of