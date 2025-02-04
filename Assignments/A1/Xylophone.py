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

# Class for Xylophone:
class Xylophone(Colourable, PercussionFamily):
    def get_name(self):
        return "Xylophone"
        
    def make_sound(self):
        return "through resonators."      
        
    def get_price(self):
        return 155.00
        
    def play_instructions(self):
        return "by hitting bars with two mallets."
        
    def how_to_repair(self):
        return "Replace the broken bars."
        
    def how_to_colour(self):
        return "Colour the bars."