from time import sleep

#This is Product Class incharge of creating the object that will be placed on the inventary
class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.subtotal = self.price * self.amount

#This is the class that has and manage the inventory
class InventoryManager:
    def __init__(self):
        self.product_list = []
        
    #In here the InventoryManager add the product object to the list
    def add_to_list(self, product_object):
        self.product_list.append(product_object)

    #In this function there is printed every single product, name, price amount and total per product
    def show_total(self):
        for product in self.product_list:
            print("Product name: ...............:",product.name)
            print("Product price: ..............:",product.price)
            print("Product cuantity: ...........:",product.amount)
            print("Product subtotal: ...........:",product.subtotal)
            print(".............................................................")
        #Also it prints the total amount spent in all of the products.
        total = sum(product.subtotal for product in self.product_list)

        for i in f"\nTotal: {total}\n":
            print(i, end="", flush=True)
            sleep(0.01)
