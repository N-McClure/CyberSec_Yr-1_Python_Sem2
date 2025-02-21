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


def json_str_to_dict():
    j_fruits = '{"a":"apple", "b":"banana", "o":"orange", "w":"watermelon"}' # just a string, not json 
    #j_fruits = '{"a":"apple", "b":"banana", "c":"cherry", "d":"date",}' # cannont be converted to json due to the trailing ','
    ##1
    # dict_fruits = json.loads(j_fruits) # convert the json string to python dictionary 
    # print(dict_fruits)

    ## 2
    try:
        dict_fruits = json.loads(j_fruits) # surround it by try to catch
        print(dict_fruits)
    except JSONDecodeError:
        print('JSON parsing error!')
    return dict_fruits


def dict_to_json_str(dict):
    print(json.dumps(dict))

def dealing_with_object():
    fruits = {'a':Fruit('apple'), 'b':Fruit('banana'), 'c':Fruit('Cherry')} # dictionary
    #print(json.dumps(fruits)) #TypeError: Object of type set is not JSON serializable, need to override the JSON encoder class's default method
    print(json.dumps(fruits, cls=FruitEncoder)) # supply the helper class encoder to serialize

if __name__ == '__main__':
    
    dict = json_str_to_dict()
    # converty python dictioinary to json 
    dict_to_json_str(dict)
    
    #print(json.dumps(dict_fruits))

    
    dealing_with_object()

