# Process JSON data received from an application
import json
from json import JSONDecodeError
if __name__ == '__main__':
    # json string recived
    json_str = '''{
            "name" : "Bob",
            "sid" : 112,
            "campus" : "Oakville",          
            "subjects" : [
                "Programming",
                "Networking",
                "Security"
            ],
            "current": true,
            "grade" : 4.5
        }'''
    
    # parse the json data as a dictionary 
    try:
        data = json.loads(json_str)
    except JSONDecodeError as err:
        print('JSON parsing error!')
    #print(data) # print the dicitonary

    # print various informaiton from the data
    print("Name: " + data['name'])
    if (data['current']): # check for current = True
        print (data['grade'])
    for s in data['subjects']:
        print(s)