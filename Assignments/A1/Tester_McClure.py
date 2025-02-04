# Assignment #: 01
# Course: PROG23199
# Developer Name: Nicholas McClure
# Student ID #: 991693366
# Due Date: 2025/02/02
# Instructor's Name: Syed Tanbeer

# My Site: https://n-mcclure.github.io/
# My GitHub: https://github.com/N-McClure
# My LinkedIn: https://www.linkedin.com/in/nick-mcclure-578565295/

# Imported Libraries, Modules, and Classes:
from MusicalInstrument import MusicalInstrument
from PercussionFamily import PercussionFamily
from StringFamily import StringFamily
from WoodwindFamily import WoodwindFamily

from Drum import Drum
from Xylophone import Xylophone
from Piano import Piano
from Guitar import Guitar
from Recorder import Recorder

from Order import Order

def menu():
    '''
    -- Implement this function to create the menu.
    -- Do not implement any business logic for any menu option here, 
    use separate function for each menu and call them as required, instead.
    '''
    
    # Display the menu options and prompt the user to enter their choice:
    print(f'***********************************************************************************')
    print(f'Musical Instrument Information System (MIIS)\n')
    print(f'1. Display Instrument Information')
    print(f'2. Sort Instruments by Price')
    print(f'3. Sort Instruments in Category by Name')
    print(f'4. Order Instruments and Special Details')
    print(f'5. Quit')
    print(f'***********************************************************************************')
    
    choice = input('Enter your option (1-5): ')
    
    # Call the corresponding function based on the user's choice:
    if choice == '1':
        display_instrument_info()
    elif choice == '2':
        sort_by_price()
    elif choice == '3':
        sort_by_name()
    elif choice == '4':
        order_management()
    elif choice == '5':
        print('Thank you for using the MIIS. Goodbye!')
        exit()
    else:
        print('Invalid option. Please try again.')
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
