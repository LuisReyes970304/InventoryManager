from messages import invalid_price_message, invalid_amount_message, invalid_name_message, invalid_ValueError_message_int, invalid_ValueError_message_float

def name_validator():
    validator = True
    while validator:
        name = input("Write the product's name: ").strip().capitalize()
        if not name:
            invalid_name_message()
            validator = True
        if name: 
            validator = False
    return name

    
def price_validator(name):
    validator = True
    while validator:
        try:
            price = float(input(f"Write the {name}'s price: "))
            if price <= 0: 
                invalid_price_message()
                validator = True
            if price > 0:
                validator = False
        except ValueError:
            invalid_ValueError_message_float()
    return price


def amount_validator(name):
    validator = True
    while validator:
        try:
            amount = int(input(f"Write the {name}'s amount: "))
            if amount <= 0: 
                invalid_amount_message()
                validator = True
            if amount > 0:
                validator = False
        except ValueError:
            invalid_ValueError_message_int()
    return amount

