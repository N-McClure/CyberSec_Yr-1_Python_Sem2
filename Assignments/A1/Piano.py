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
from StringFamily import StringFamily

# Class for Piano
class Piano(Colourable, PercussionFamily, StringFamily):
        
    def get_name(self):
        return "Piano"
        
    def make_sound(self):
        return "by vibrating the string."
        
    def get_price(self):
        return 739.99
        
    def play_instructions(self):
        return "by hitting the key bars."
        
    def how_to_repair(self):
        return "Replace the broken strings or keys."
        
    def how_to_colour(self):
        return "Colour the base and sides."