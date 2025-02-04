# Assignment #: 01
# Course: PROG23199
# Developer Name: Nicholas McClure
# Student ID #: 991693366
# Due Date: 2025/02/02
# Instructor's Name: Syed Tanbeer

# My Site: https://n-mcclure.github.io/
# My GitHub: https://github.com/N-McClure
# My LinkedIn: https://www.linkedin.com/in/nick-mcclure-578565295/

# Imported Libraries and Modules:
from dataclasses import dataclass

@dataclass
class Order:
    order_id: int
    customer_name: str
    instrument_list: list[str]
    
    def get_order_id(self): 
        return self.order_id
    
    def get_customer_name(self):
        return self.customer_name
    
    def get_orders(self):
        return self.instrument_list
    
    def __post_init__(self):
        self.order = self.order_id, self.customer_name, self.instrument_list