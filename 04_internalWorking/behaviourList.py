l1 = [1,2,3]
l2 = l1
l1[0] = 5
print(l1)  # Output: [5, 2, 3]
print(l2)  # Output: [5, 2, 3]

l3 = [1,2,3]
l4 = l3
l3 = "hello"
print(l4)  # Output: hello

# when the data type is mutable python will create a new re

# when the data type is immutable python will not create a new reference else just point to the same object with same value



# When the data type is immutable, like an integer or string, Python may point multiple variables with the same value to the same memory location (since the value can't be changed).
# When the data type is mutable, like a list or dictionary, Python creates a new object each time, even if the values are the same — because the values can change.

h1 = [1, 2, 3]
h2 = h1.copy()  # Creates a shallow copy of the list
h1[0] = 5
print(h1)  # Output: [5, 2, 3]
print(h2)  # Output: [1, 2, 3]

# the diff between copy and deepcopy is list & nested list 


# is ... can check if the object are having the same reference or not
print(h1 is h2)  # Output: False, because they are different objects in memory