friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(friends)
print(friends[-1])  
print(friends[len(friends) - 1])
print(friends[:2])
friends.append("Frank")
print(friends)
friends[1:2] = ["Zoe"]
print(friends)
print(friends[1:1])

friends[1:3] = []
print(friends)

for friend in friends:
    print(friend , end=" ") 

if "Eve" in friends:
    print("\nEve is in the list.")

else:
    print("\nEve is not in the list.")

friends.insert(2, "Grace")
print(friends)
friends.append("Hannah")
print(friends)  
friends.remove("Alice")
print(friends)  
friends.pop(1)
print(friends)

tea = ["Green", "Black", "Oolong", "White"]
teaCopy = tea
print(teaCopy)
tea[1] = "Herbal"
print(teaCopy)  # This will also show the change because teaCopy is a reference to the same list

square = [ x**2 for x in range(1, 11)]
print(square)