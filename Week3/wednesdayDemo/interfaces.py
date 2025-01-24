from abc import ABC, abstractmethod
class Weighable(ABC):
    
    @abstractmethod
    def get_weight(self):
        pass

class Edible(ABC):
    
    @abstractmethod
    def how_to_eat(self):
        pass