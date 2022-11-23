"""
An script based app for self-service cashier service
Customer can do the following thing:
1. Add item details:
    - add item name
    - add item quantity
    - add item price
"""

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    quantity: int
    price: float


class Transaction:
    """
    Class to record for each transaction
    """

    def __init__(self):
        self.products = {}
        self.product_names = []

    def product_exists(self, name):
        """
        Check if a product is already exists in the list(self.product_names)

        INPUT: name
        OUTPUT:
            True if product is already exists
            False if product is not exists

        USAGE:
            Adding item
            Update new name, quantity, and price
            Remove item

        """
        if name in self.product_names:
            return True
        else:
            return False

    def product_not_exists(self, name):
        """
        Check if a product is NOT exists in the list(self.product_names)

        INPUT: name
        OUTPUT:
            True if product is NOT already exists
            False if product is exists

        USAGE:
            Update new name

        """
        if name not in self.product_names:
            return True
        else:
            return False

    def add_item(self, name, quantity, price):
        """
        Add a new item: item name, item quantity, and item price

        INPUT: name, quantity, price
        OUTPUT:
            Return True if the item was added
            Return False if the item was NOT added

        FLOW:
            1. Check if product is already exists
            2. Validate product:
                    - If Exists, do not add the item: Return False
                    - If not,
                        add item: name, quantity, price to hash map (self.products)
                        add item: name to list (self.product_names)
                        Return True
        """
        product_exists = self.product_exists(name)
        if product_exists:
            print(False)
        else:
            self.products[len(self.product_names)] = Product(name, quantity, price)
            # for update name
            self.product_names.append(name)
            print(True)

    def update_name(self, name, new_name):
        """
        Update the name of the product

        INPUT: name, new name
        OUTPUT:
            Return True if name successfully updated
            Return False if name NOT successfully updated

        FLOW:
            1. Validate product:
                - Check if the product name is already exists:
                    Return True if exists, otherwise return False
                - Check if the product NEW name is not exists:
                    Return True if not exists, otherwise return False
            2. IF 2 conditional are met (both True):
                    - get the index of the product from the list (self.product_names)
                    - use index to replace the name to new name in the hash map (self.products)
                    - replace the name with the new name in the list (self.product_names)
                    - Return True
                Otherwise:
                    - Return False
        """
        from dataclasses import replace

        product_exists = self.product_exists(name)
        product_not_exists = self.product_not_exists(new_name)

        if product_exists and product_not_exists:
            idx = self.product_names.index(name)
            self.products[idx] = replace(self.products[idx], name=new_name)
            self.product_names[idx] = new_name
            print(True)
        else:
            print(False)

    def update_quantity(self, name, new_quantity):
        from dataclasses import replace

        product_exists = self.product_exists(name)
        if product_exists:
            idx = self.product_names.index(name)
            self.products[idx] = replace(self.products[idx], quantity=new_quantity)
            print(True)
        else:
            print(False)

    def update_price(self, name, new_price):
        """
        Update the price of a product

        INPUT: name, new price
        OUTPUT:
            Return True if successfully updated the price
            Return False if NOT successfully updated the price

        FLOW:
            1. Check if the product is already exists
            2. IF it exists:
                    - get index of the product from the list (self.product_names)
                    - replace the product price with the new price
                    - Return True
                Otherwise:
                    - Return False
        """
        from dataclasses import replace

        product_exists = self.product_exists(name)
        if product_exists:
            idx = self.product_names.index(name)
            self.products[idx] = replace(self.products[idx], price=new_price)
            print(True)
        else:
            print(False)

    # Try to find a way to allow multiple remove of items
    def remove_item(self, name):
        """
        Remove a single item of product using the given name

        INPUT: name
        OUTPUT: Return True if the item was removed, False otherwise

        FLOW:
            1. Check if the product exists
            2. If exists:
                    - Get the index of the product to be removed
                    - Get the index of the last index of list (self.product_names)
                    - Replace the product to be removed with the last product in the list
                    - Remove the last product from the list

                    - Replace the product to be removed with the last product in the hash map (self.products)
                    - Delete the last product from the hash map
                    - Return True
                Otherwise:
                    - Return False
        """
        product_exists = self.product_exists(name)
        if product_exists:
            target_idx = self.product_names.index(name)
            last_val_idx = len(self.product_names) - 1
            last_val = self.product_names[last_val_idx]
            self.product_names[target_idx] = last_val
            self.product_names.pop()
            self.products[target_idx] = self.products[last_val_idx]
            del self.products[last_val_idx]
            print(True)
        else:
            print(False)

    def printa(self):
        """
        Show test cases results
        """
        print()
        for i, v in self.products.items():
            print(i, v)
        print()
        print(list(self.products.keys()))
        print(self.product_names)


def main():
    transact_123 = Transaction()
    transact_123.printa()
    transact_123.add_item("mask", 2, 1300.99)
    transact_123.add_item("shoes", 1, 5000)
    transact_123.printa()
    transact_123.remove_item("mask")
    transact_123.printa()


if __name__ == "__main__":
    main()
