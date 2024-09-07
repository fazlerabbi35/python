######### Avg making calculator (1 -32)

"""num = int(input("How many numbers?"))
total_sum = 0

for n in range(num):
    numbers = float(input("Enter your number: "))
    total_sum += numbers

avg =    total_sum / num
print("The average is", avg)"""


"""num = int(input("How many numbers?"))
total_sum = 0

for n in range(num):
    numbers= float(input("Enter your number: "))
    total_sum += numbers

avg = total_sum / num
print("The average is ", avg)"""

"""week = int(input("How many days: "))
sum_temp = 0

for w in range(week):
    temp = float(input("Enter the temperatur: "))
    sum_temp += temp

avg = sum_temp / week
print(avg)"""





##  (38-71) It will give you a short message if you don't fill the condition.
"""name = input("Enter your name: ")

if name == "":
    print("You didn't enter your name.")
else:
    print(f"Hello {name}")
"""

"""
name = input ("Enter your name: ")

while name == "":
    print("You didn't enter your name.")
    name = input("Please enter your name first: ")
print(f"Good Day! {name}")"""


"""
identity = input("Enter your password: ")

while identity == '':
    print("You didn't enter your password")
    identity = input("Enter your password: ")
print("Congratulations! You get the access!")
"""

"""
name = input("Enter your name: ")

while name == '':
    print("You didn't enter your name.")
    name = input("Please enter your name first: ")
    print(f"Hello Mr {name} good morning!")"""







#It will make a corona virus image#####
"""from turtle import *
color('green')
bgcolor('black')
speed(1)
hideturtle() 
b=0
while(b<200):
    right(b)
    forward(b*2)
    b+=1"""





#####  1   FIND THE MAX NUMBER

"""def max_three (x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

print(max_three(12, 52, 91))"""





#### 2  Sum of all numbers

"""def  sum(numbers):
    total = 0

    for x in numbers:
        total += x
    return total
print(sum((4, 3, 5, 3, 9, 24)))"""


"""
def jogfol(songka):
    total = 0

    for k in songka:
        total += k

    return total
print(jogfol((8, 43, 2, 7)))"""