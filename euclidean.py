import random

# generate 2 random numbers from 1 to 1500
a, b = random.randint(1, 1500), random.randint(1, 1500)
print (a, b)

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)
