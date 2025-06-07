import math
import random
from decimal import Decimal
from fractions import Fraction


x = 2
y = 3
print(x**y)


print((x + y) // 3)

# always use parentheses to make the order of operations clear
#always try to keep the data types consistent while performing operations

print(40 + int(2.5))  # 42

print(x,y)

print(x%2)

print(2**100)

result = 1.0/ 3.0
print(result)

print(1< 2)


print(1 < 2 < 3)  
# to inc the readability of the code, use and operator to chain comparisons

print(1 < 2 and 4 < 3)

print(1 == 2 < 3)

print(math.sqrt(16))  # 4.0

print(math.floor(-2.5))  # -3 //floor rounds down to the nearest integer

print(math.trunc(-2.5))  # -2

# trunc -> 0 # truncation removes the decimal part, leaving only the integer part

print(0o10)
print(0x10)
print(0b10)
print(bin(10))
print(int('001',2)) # base and number to be converted 

print(random.choice([1,2,4,5,6,8,9,10]) ) # generates a random float between 0.0 and 1.0

print(random.randint(1, 4))  # generates a random integer between 1 and 10

lis = [1, 2, 3, 4, 5]
random.shuffle(lis)
print(lis)  # shuffles the list in place


print(0.1+0.1+0.1-0.3)  # 5.551115123125783e-17, due to floating point precision issues

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))  # 0.0

myfra = Fraction(1, 4) - Fraction(1, 5)
print(myfra) # 1/20



set1 = {1,2,3,4,3,2,1,5,6,7,8,9,10}
print(set1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} - set removes duplicates
set2 = { 2, 4,  6,  8,  11}

print(set1 & set2)  # intersection of two sets {2, 4, 6, 8}
print(set1 | set2)  # union of two sets {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

print(type({}))

print(type(True))

print(True + True)  # 2, True is treated as 1 and False as 0 in arithmetic operations