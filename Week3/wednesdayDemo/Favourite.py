class Favourite:
    def __init__(self, person):
        self.person = person # this is called a "Composition".
        self.favourite_list = []
    
    def add_to_favourite(self, item):
        return self.favourite_list.append(item)
    
    def get_favourite_list(self):
        return self.favourite_list