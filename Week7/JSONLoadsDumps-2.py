# Process JSON data received from an application
import json

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
    data = json.loads(json_str)
    #print(data) # print the dicitonary

    # print various informaiton from the data
    print("Name: " + data['name'])
    if (data['current']):
        print (data['grade'])
    for s in data['subjects']:
        print(s)