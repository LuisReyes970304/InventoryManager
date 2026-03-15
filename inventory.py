from time import sleep

class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.subtotal = self.price * self.amount


class InventoryManager:
    def __init__(self):
        self.product_list = []
        
    def add_to_list(self, product_class):
        self.product_list.append(product_class)

    def show_total(self):
        for product in self.product_list:
            print("Product name: ...............:",product.name)
            print("Product price: ..............:",product.price)
            print("Product cuantity: ...........:",product.amount)
            print("Product subtotal: ...........:",product.subtotal)
            print(".............................................................")
        total = sum(product.subtotal for product in self.product_list)

        for i in f"\nTotal: {total}\n":
            print(i, end="", flush=True)
            sleep(0.01)
