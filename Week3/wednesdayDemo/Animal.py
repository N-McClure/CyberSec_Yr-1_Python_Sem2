from abc import ABC, abstractmethod
from interfaces import Weighable
#class Animal(ABC, Weighable): # will not work, the ABC has to be the last one
class Animal(Weighable, ABC): # ABC should be listed at the end
    @abstractmethod
    def make_sound(self):
        pass
    
    
 