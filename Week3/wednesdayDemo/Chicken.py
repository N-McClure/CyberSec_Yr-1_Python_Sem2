from Animal import Animal
from interfaces import Edible

class Chicken(Animal, Edible): 
    def make_sound(self):
        print('Chik! Chik!')
    
    def how_to_eat(self):
        print('Make chicken fry.')
    
    def get_weight(self):
        return 4
    
    def get_name(self):
        return 'Chicken'
    
 