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
    
class Repairable(ABC):
    @abstractmethod
    def how_to_repair(self):
        pass
    
class Colourable(ABC):
    @abstractmethod
    def how_to_colour(self):
        pass