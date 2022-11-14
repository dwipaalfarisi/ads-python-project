'''
An script based app for self-service cashier service
Customer can do the following thing:
1. Add item details:
    - add item name
    - add item quantity
    - add item price
'''

class Transaction:
    '''
    USE DATACLASS??????
    '''
    def add_item(item_name: str=None, item_quantity: int=None, item_price: float=None):
        '''
        Add item:
            item_name
            item_amount
            item_price 
        '''
        flag=True
        while flag:
            item_name = str(input("What's the item you want to add?"))
            item_quantity = int(input("How many item you want to add?"))
            item_price = float(input("What's the item price?"))
            flag=False

        print(item_name, item_quantity, item_price)

if __name__ == "__main__":
    Transaction.add_item()