def menu():
    '''
    -- Implement this function to create the menu.
    -- Do not implement any business logic for any menu option here, 
    use separate function for each menu and call them as required, instead.
    '''

def get_instruments():
    '''
    -- Implement this function to create all instruments and return a list containing the instruments.
    '''

def display_instrument_info():
    '''
    -- Implement this function to display detail information for each instrument 
    i.e., business logic for the menu item (1. Display Instrument Information) should be implemented here.
    -- Use the instrument list alreday created in get_instruments() function.
    '''

def sort_by_price():
    '''
    -- Implement this function to sort the instruments by price.
    -- This function should be invoked for the 2nd menu item (i.e., 2. Sort Instruments by Price')
    -- Use the instrument list already created in get_instruments() function.
    '''

def sort_by_name():
    '''
    -- Implement the business logic for menu item 3 (i.e.,  3. Sort Instruments in Category by Name) in this function.
    -- Use the instrument list already created in get_instruments() function.
    '''
    
def order_management():
    '''
    -- Implement this function to support the 4th menu item (i.e., 4. Order Instruments and Special Details).
    -- Use the instrument list already created in get_instruments() function, if needed.
    -- To process and display the special features of the instruments in the order list, use a separate function called display_features(order_list).
    '''
    
def display_features(ordered_instruments: list):
    '''
    -- This function should receive a list containing the instruments ordered by a customer.
    -- It should programmatically extract the special feature information of each instruemnt in the list and display to the user.
    '''
    
if __name__ == '__main__':
    menu() 
