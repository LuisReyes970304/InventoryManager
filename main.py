#This is the main file in which run all the program. 
from inventory import InventoryManager, Product
from messages import welcome_message_fun
from validation import name_validator, price_validator, amount_validator   
from time import sleep


welcome_message_fun()

name = name_validator()
price = price_validator(name)
amount = amount_validator(name)

product = Product(name, price, amount)
app = InventoryManager()

active = True
while active:
    app.add_to_list(product)
    another_product = input("\nDo you want to add another product? (yes/not): ").lower()
    if another_product == "yes":
        name = name_validator()
        price = price_validator(name)
        amount = amount_validator(name)
        product = Product(name, price, amount)
    elif another_product != "yes":
        active = False

app.show_total()
    


