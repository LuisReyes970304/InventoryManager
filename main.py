#This is the main file in which run all the program. 
from time import sleep
from model import InventoryManager

welcome_message = """

******************** Welcome to InventoryManger ********************

********** This is a simple program that works in console **********

********************** Les't start  with this **********************

"""
for i in welcome_message:
    print(i, end="", flush=True)
    sleep(0.01)


active = True
while active:
    app = InventoryManager()
    app.add_to_list()
    continue_message = input("\nDo you want to add another product? (yes/no): ")
    if continue_message.lower() != "yes":
        active = False    
    else:
        app.name = input("Provide the product name: ")
        app.price = float(input(f"Provide the {app.name}'s price: "))
        app.amount = int(input(f"Provide the {app.name}'s amount: "))
        app.subtotal = app.price * app.amount

app.show_total()
    
print("\nThank you for using InventoryManager. Goodbye!")