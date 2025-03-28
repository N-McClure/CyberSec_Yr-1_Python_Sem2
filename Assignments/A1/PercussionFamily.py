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

class PercussionFamily(MusicalInstrument, Repairable):
    def __init__(self, num_of_keys):
        super().__init__()
        self.num_of_keys = num_of_keys
        
    def get_num_of_keys(self):
        return self.num_of_keys