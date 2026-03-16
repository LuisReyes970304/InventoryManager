#This is the main file in which run all the functions. 
from inventory import InventoryManager, Product
from messages import welcome_message_fun, bye_message_function
from validation import name_validator, price_validator, amount_validator

#Welcome message
welcome_message_fun()

#Inputs for name, price and amount
name = name_validator()
price = price_validator(name)
amount = amount_validator(name)

#In here the product object
product = Product(name, price, amount)

#The InventoryManager is instantiated
app = InventoryManager()

#Start of the loop
active = True
while active:
    #The product is added to the list
    app.add_to_list(product)
    #Ask for another productt to be added
    another_product = input("\nDo you want to add another product? (yes/not): ").lower()
    if another_product == "yes":
        print("")
        #If yes, is needed to declare the inputs again so the former information product is not added one more time to the list, but the new one yes.
        name = name_validator()
        price = price_validator(name)
        amount = amount_validator(name)
        product = Product(name, price, amount)
    elif another_product != "yes":
        active = False

#Onces the app stop, it calculate the total an show it. 
app.show_total()

#Bye message
bye_message_function()
    


