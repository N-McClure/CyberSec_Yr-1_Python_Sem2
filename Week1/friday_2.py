class Item:
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price
    
    # Setters:
    # - Use the setDiscount method to set a discount for specific items.
    def setDiscount(self, discount):
        self._discount = discount
        
    # - Get the discount if the _discount attribute is set...else...regular price.
    def getPrice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price
        
def main():
    apple = Item(1, 'apple', 10)
    orange = Item(2, 'orange', 2.2)
    apple.setDiscount(0.50)
    orange.setDiscount(0.25)
       
    print(f'Apple price: {apple.getPrice()}')
    print(f'Orange price: {orange.getPrice()}')
    
main()