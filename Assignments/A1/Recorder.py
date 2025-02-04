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
from interfaces import Colourable
from WoodwindFamily import WoodwindFamily

# Class for Recorder:
class Recorder(Colourable, WoodwindFamily):
    def __init__(self, made_of):
        self.made_of = "Wood"
            
    def get_name(self):
        return "Recorder"
        
    def make_sound(self):
        return "in a manner of a whistle or an organ flue pipe."
        
    def get_price(self):
        return 190.00
        
    def play_instructions(self):
        return "by blowing a gentle stream of it through the mouthpiece."
        
    def how_to_colour(self):
        return "Colour both sides." 