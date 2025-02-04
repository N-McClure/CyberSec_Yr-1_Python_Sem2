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
from PercussionFamily import PercussionFamily

# Class for Drum:
class Drum(Colourable, PercussionFamily):
    def __init__(self, diameter_in_inch):
        self.diameter_in_inch = diameter_in_inch
        
    def get_diameter_in_inch(self):
        return self.diameter_in_inch
        
    def get_name(self):
        return "Drum"
        
    def make_sound(self):
        return "by vibrating stretched membrane."
        
    def get_price(self):
        return 353.99
        
    def play_instructions(self):
        return "by hitting the membrane with sticks."
        
    def how_to_repair(self):
        return "Replace the membrane."
        
    def how_to_colour(self):
        return "Colour the sides and stands."