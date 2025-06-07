# in python every memory allocation has a reference count
# when the reference count reaches zero, the memory is freed
# this is called garbage collection

# there is no datatype for variables in python

# python does not collect garbage immediately for numbers & strings

a = 5
b = 2
a = a + 2
print(a)  

mylist = [1, 2, 3]
mylist[0] = 5
print(mylist)

#in list even if we work with same reference, it will create a new object