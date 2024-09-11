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




## 3  multipication

"""def multply (numbers):
    total = 1

    for k in numbers:
        total *= k
    return total
print(multply((4, 8, 2, 1, 10)))"""

"""
def gunfall(songka):
    hati = 1
    for h in songka:
        hati *= h
    return(hati)
print(gunfall((2, 4, 5, 5, 9)))
"""





### 4 Reverse a STRING
"""
def string_reverse(str1):
    retr1 = ''

    index = len(str1)

    while index > 0:
        retr1 += str1[index -1]

        index = index - 1

    return retr1"""





## 5  Number in a range
"""
def test_range(n):
    if n in range(3, 9):
        print("%s is in the range " %str(n))
    else:
        print("The number is outside the given range")

test_range(5)"""



## 7 Calculate the Number
"""
def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}

    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass

    print("Original String: ", s)

    print("No, of Upper case characters: ", d["UPPER_CASE"])

    print("No. of lower case Characters: ", d["LOWER_CASE"])
string_test("Fazle Rabbi")

# another one
def string(s):
    a = 0
    b = 0

    for c in s:
        if c.isupper():
            a += 1
        elif c.islower():
            b += 1
        else:
            pass
    
    print("Original String: ", s)
    print("No of upper case: ", a)
    print("No of lower case: ", b)
string("My name is MD Fazle Rabbi")"""



####  8 takes a list and returns a new distinct list
"""
def list_1(l):
    x = []

    for k in l:
        if k not in x:
            x.append(k)

    return x
print(list_1([1,2,4, 8, 4, 3,5,4])

## Another one

def my_fun(x_list):
    y_list = []

    for x in x_list:
        if x not in y_list:
            y_list.append(x)
    return y_list
print(my_fun([1,1,1,2,3,4,4,4,5,6,5,5,9]))"""



### 9 it's pirme or not
"""def test_prime(n):

    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
print(test_prime(9))


from math import sqrt
def is_prime(num):
    if num <= 1 or (num % 2 == 0 and num > 2):
        return False
    return all (num % i for i in range(3, int(sqrt(num)) +1, 2))


print(is_prime(11))
print(is_prime(18))"""


"""
## 10 Find a even number list
def even_test(n):
    e_lsit = []

    for k in n:
        if k % 2 == 0:
            e_lsit.append(k)
    return e_lsit
print(even_test([1,2,4,5,4, 9, 3]))"""



















## 12 Wheter a passed string is a palindrome or not
"""
def is_palindrome(string):
    left_pass = 0
    right_pass = len(string) -1

    while right_pass >= left_pass:
        if not string[left_pass] == string[right_pass]:
            return False
        
        left_pass += 1
        right_pass -= 1

    return True

print(is_palindrome('madamimadam'))"""















### 13 print a list where the number is in the square list
"""
def printValues():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l)
printValues()"""


# 14  print a list where the number is in the square root list
"""
def R_root():
    m = list(range(1, 60))
    l = list()

    for k in m:
        for i in m:
            if (k**0.5)==i:
                l.append(i)
    print(l)
R_root()"""


## 15 
"""

def test(a):
    def add(b):
        nonlocal a
        a += 6
        
        return a+b
    return add
func = test(4)
print(func(4))"""

