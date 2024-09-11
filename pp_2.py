"""import random

name = input("what's your name? ")
print("Good luck!", name)


words = ["Ramos", "Ronaldo", "Xabi", "Kross", "Modric", 
         "pepe", "Casials", "Navas", "James", "Ozil", 
         "Benzema", "Bale", "Marcelo", "Casemiro", "kaka",
         "Valverde", "Carvajal", "Camavinga", "Rodrigo", 
         "Vini", "Mbappe", "Belingham"]

word = random.choice(words)
print("Guess the character")

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed +=1

    if failed == 0:
        print("You win!")
        print("The word is ", word)
        break

    print()
    guess = input("guess a character: ")
    guesses += guess

    if guess not in word:
        turns -=1

        print("wrong")
        print("You have ", +turns, "more guesses")

        if turns == 0:
            print("You loose!")
"""



"""
def sum(numbers):
    total = 0

    for k in numbers:
        total += k
    return total
print(sum((34, 2, 4, 20, 17, 13)))"""

"""def sum(*numbers):
       total = 0
        for i in numbers:
            total += i
        return total
print(sum(3, 5, 9, 2))
def multiply(numbers):
    multi = 1
    for k in numbers:
        multi *= k 
    return multi"""


"""
def r_string(string):

    r_str = ''

    index = len(string)

    while index > 0:
        r_str += string[index -1]

        index = index -1
    return r_str
print(r_string("abcd"))




def my_fun(string):
    string_2 = ''
    index = len(string)

    while index > 0:
        string_2 += string[index -1]
        index = index -1
    return string_2
print(my_fun("Rabbi"))
"""


"""
##### 4
def reverse_str(string):
    r_str = ''
    index = len(string)

    while index > 0:
        r_str += string[index -1]

        index = index -1
    return r_str
print(reverse_str("MyName"))


def name(apple):
    r_name = ''

    counter = len(apple)

    while counter > 0:
        r_name += apple[counter -1]
        counter = counter -1
    return r_name
print(name("APPLE"))"""

"""
def multiply(numbers):
    total = 1

    for k in numbers:
        total *= k
    return total
print(multiply((12, 2, 5, 3, 5 )))



def sum(numbers):
    total = 0
    for s in numbers:
        total += s

    return total
print(sum((12, 5, 13, 5, 15)))


def max_finder(numbers):
    total = 0
    for k in numbers:
        return k
    
print(max_finder((12, 4, 35, 94)))

 """















"""
def test_range(n):
    if n in (3 ,9):
        print("%s in the range" %str(n))
    else:
        print("%s The number is not in that list" %str(n))
test_range(96)


def test_range(k):
    if k in range(1, 20):
        print("%s in the range" %str(k))
    else:
        print("%s is not on that list" %str(k))
test_range(121)
"""




"""def string(s):
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



"""
def x_list(list_s):
    list_n = []

    for a in list_s:
        if a not in list_n:
            list_n.append(a)
    return list_n
print(x_list([1,2,5,5,2]))



def my_fun(x_list):
    y_list = []

    for x in x_list:
        if x not in y_list:
            y_list.append(x)
    return y_list
print(my_fun([1,1,1,2,3,4,4,4,5,6,5,5,9]))"""

"""
def test_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
print(test_prime(1))
            


from math import sqrt

def is_prime(num):
    if num <=1 or (num % 2 == 0 and num >2):
        return False
    return all (num % i for i in range(3, int(sqrt(num)) +1, 2))

print(is_prime(229))


from math import sqrt

def is_prime(n):
    if n <= 1 or (n > 2 and n % 2 == 0):
        return False
    return all( n % k for k in range(3, int(sqrt(n)) +1, 2))

print(is_prime(12))

"""


"""

def values():
    l = list()

    for i in range(1, 10):
        l.append(i**3)
    print(l)
values()
"""
"""

def root():
    m = list(range(1,10))
    r = list()

    for k in m:
        
root()
"""

### it will give you a range of certain number square root form


""" 
m = list(range(1,40))
l = list()
for i in m:
    for k in m:
        if (k**0.5) == i:
            l.append(i)
            print(l)"""

def R_root():
    m = list(range(1, 60))
    l = list()

    for k in m:
        for i in m:
            if (k**0.5)==i:
                l.append(i)
    print(l)
R_root()






"""
numbers = [12, 4, 35, 94]
for k in numbers:
    print(k)"""
   