# random module, numbers, f str, for loop, enumrtate,reversered
import random

x,y,z = 23,43,98

print(f" x={x} \n y={y} \n z={z}")

no = random.randint(1,11)
print(f"random no is: {no}")

print(type(no))

list =[3,4,6,2,9]
for x in list:
    print(f"loop x value is: {x}")

for x in range(10):
    print(x)

print(reversed("abcd"))