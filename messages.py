from time import sleep

welcome_message = """

******************** Welcome to InventoryManger ********************

********** This is a simple program that works in console **********

********************** Les't start  with this **********************

"""

value_error_float = """
       **********************************
         Invalid product price!!!
         Price has to be a float.
       **********************************
         Please try again:

"""

value_error_integer = """
       **********************************
         Invalid product amount!!!
         Amount has to be a integer.
       **********************************
         Please try again:   

"""

invalid_name = """
       **********************************
         Invalid product name!!!
         Product name cannot be Empty.
       **********************************
         Please try again:

"""

invalid_amount = """
       **********************************
         Invalid product amount!!!
         cannot be a negative number.
       **********************************
         Please try again:

"""


invalid_price = """
       **********************************
         Invalid product price!!!
         Price cannot be negative.
       **********************************
         Please try again:

"""

bay_message = """
****************************************************************

         Thank you for using InventoryManager. Goodbye!

****************************************************************
"""

def welcome_message_fun():
    for i in welcome_message:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_name_message():     
    for i in invalid_name:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_amount_message():     
    for i in invalid_amount:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_price_message():     
    for i in invalid_price:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_ValueError_message_int():     
    for i in value_error_integer:
        print(i, end="", flush=True)
        sleep(0.01)

def invalid_ValueError_message_float():
    for i in value_error_float:
        print(i, end="", flush=True)
        sleep(0.01)
