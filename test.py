database = {}

def create_user(email, password):
    user = {}
    user.update({"email": email, "password": password})
    return user

user = create_user("juan@gmail.com", "1234")
user_2 = create_user("pepe@gmail.com", "5678")

def add_to_db(id: int, user: dict):
    global database
    database[id] = user
    return database

print(add_to_db(1, user))
print(add_to_db(2, user_2))