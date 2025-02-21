# Process a dictionary as JSON
import json

if __name__ == '__main__':
    # Python data
    data ={
            "name" : "Bob",
            "sid" : 112,
            "campus" : "Oakville",          
            "subjects" : [
                "Programming",
                "Networking",
                "Security"
            ],
            "current": True,
            "grade" : 4.5
        } # it's a dictiionary
    # serialize dictionary data to JSON 
    #json_str = json.dumps(data)
    json_str = json.dumps(data, indent=2)
    print(json_str)