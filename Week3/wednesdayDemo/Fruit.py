from abc import ABC, abstractmethod
from interfaces import Edible, Weighable
#class Fruit(ABC, Edible, Weighable): # will not work, the ABC has to be the last one
class Fruit(Edible, Weighable, ABC): # ABC should be listed at the end
    @abstractmethod
    def get_price(self):
        pass
    
    def __ge__(self, o):
        return self.get_price() >= o.get_price()
    
    def __lt__(self, o):
        return self.get_price() < o.get_price()
    
    
 