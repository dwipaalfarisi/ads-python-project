"""
An script based app for self-service cashier service
Customer can do the following thing:
1. Add item details:
    - add item name
    - add item quantity
    - add item price
"""
import pandas as pd

def add_user(user_id, user_pass):
    employee = {user_id: user_pass}
    return employee

def save_user():
    _user = add_user()
    

def read_user():
    # read json/csv

def login(emp_id, user_pass):
    # use conditional from read_user 

class Transaction:
    """
    Class for all transactions
    """
    def add_item(
        item_name: str = None, item_quantity: int = None, item_price: float = None
    ):
        """
        Add item:
            item_name
            item_amount
            item_price
        """
        flag = True
        while flag:
            item_name = str(input("What's the item you want to add?"))
            item_quantity = int(input("How many item you want to add?"))
            item_price = float(input("What's the item price?"))
            flag = False

        print(item_name, item_quantity, item_price)

def main():
    #run user validation first
    # then run order


if __name__ == "__main__":
    # Transaction.add_item()
    save_user()
