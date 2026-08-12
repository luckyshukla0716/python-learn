#Constructor class User 
"""Constructor is a special method in Python classes that is automatically called when an object of the class is created. 
It is used to initialize the attributes of the class."""

class User: #class User
    #pass #pass statement is used to define an empty class
    def __init__(self, user_id, name): #constructor of class User
        self.id = user_id #attribute id of class User
        self.name = name #attribute name of class User

user1 = User("001", "Lucky Shukla") #object of class User
user2 = User("002", "Abhishek") #object of class User

#print(user1.id) #print attribute id of object user1
#print(user1.name) #print attribute name of object user1 
print(f"User 1: {user1.id}, {user1.name}")

#print(user2.id) #print attribute id of object user2
#print(user2.name) #print attribute name of object user2
print(f"User 2: {user2.id}, {user2.name}")

#print(f"User 1: {user1.id}, {user1.name}\nUser 2: {user2.id}, {user2.name}") #print attribute id and name of object user1 and user2

