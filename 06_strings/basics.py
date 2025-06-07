str = "yashveer dalal  "
print(str)
print(str[0])
name = str[0:9]
print(name)
surname = str[-1]
print(surname)  

numberList = "0123456789"
print(numberList[5:])
print(numberList[:5])
print(numberList[0:8:2])
print(str.capitalize())
print(str.upper())
str.strip()
print(str.replace("yashveer", "rana"))

friends = "yashveer, ranveer, anshul, deepanshu, akash"
print(friends.split(", "))

print(friends.find("ranveer"))

print(friends.count
      ("anshul"))


gift  = "toy car"
quantity = 5
print(f"I want to buy {quantity*5} {gift}s for my birthday")

enemies = ["john", "doe", "jane"]
print(" ".join(enemies))

print(len(name))

for letter in str:
    print(letter, end=" ")
    

sentence = 'I love "python" programming'
sentence2 = "I love \"python\" programming"

print("yash\nveer")
print(r"yash\nveer")
  # raw string, no escape sequences processed

print("yash\\nveer")

print("yashveer" in str) 