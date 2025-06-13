friends = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "hiking", "coding"],
    "is_student": False,}

print(friends["name"])
print(friends.get("name")) # Accessing a value using a key

print(friends)


for friend in friends:
    print(friend, friends[friend])  # Prints the keys

for key, value in friends.items():
    print(key, value)  # Prints both keys and values        

if "name" in friends:
    print("Name is present in the dictionary.") 

friends["address"] = "123 Main St"  # Adding a new key-value pair
print(friends)

friends.pop("age")  # Removing a key-value pair
print(friends)
print("\n")
print("\n")
del friends["city"]  # Deleting a key-value pair
print(friends)

print("\n")

friendsCopy = friends.copy()  # Creating a copy of the dictionary
print(friendsCopy)  

tea_shop ={
    "chai" : {"ginger" : "zesty" , "milk" : "creamy", "sugar" : "sweet"},
    "coffee" : {"milk" : "frothy", "sugar" : "sweet"},
    "pastry" : {"flavor" : "buttery", "topping" : "sprinkles"}
}

print(tea_shop["chai"]["ginger"])  # Accessing nested dictionary values

squared_numbers = {x: x**2 for x in range(1, 6)}  # Dictionary comprehension
print(squared_numbers)  # Prints {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squared_numbers.clear()