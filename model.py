#This is the main model for objects!

#This is the model that create the product dict
from time import sleep
class Inventory:
    def __init__(self):
        self.name = input("Provide the product name: ")
        self.price = float(input(f"Provide the {self.name}'s price: "))
        self.amount = int(input(f"Provide the {self.name}'s amount: "))

        self.subtotal = self.price * self.amount

    def create_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "amount": self.amount,
            "subtotal": self.subtotal
        }
    
class InventoryManager(Inventory):
    def __init__(self):
        super().__init__()
        self.product_list = []
        
    def add_to_list(self):
        product_dict = self.create_dict()
        self.product_list.append(product_dict)
        return self.product_list
    
    def show_total(self):
        for i in range(len(self.product_list)):
            info = self.product_list[i]
            print(f"\nProduct {i + 1}:\n")
            print("Product name: ...............:",info["name"])
            print("Product price: ..............:",info["price"])
            print("Product cuantity: ...........:",info["amount"])
            print("Product subtotal: ...........:",info["subtotal"])
            print(".............................................................")
        total = sum(product["subtotal"] for product in self.product_list)
        for i in f"\nTotal: {total}":
            print(i, end="", flush=True)
            sleep(0.01)
