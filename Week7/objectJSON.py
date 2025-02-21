import json
from json import JSONDecodeError, JSONEncoder
class Fruit:
    def __init__(self, name) -> None:
        self.name = name

# create a helper class to encode Fruit to serializable and understandable to json
class FruitEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Fruit:
            return o.name
        return super().default(o) 

def dealing_with_object():
    fruits = {'a':Fruit('apple'), 'b':Fruit('banana'), 'c':Fruit('Cherry')}
    #print(json.dumps(fruits)) #TypeError: Object of type set is not JSON serializable, need to override the JSON encoder class's default method
    print(json.dumps(fruits, cls=FruitEncoder)) # supply the helper class encoder to serialize

if __name__ == '__main__':
    
      
    dealing_with_object()

