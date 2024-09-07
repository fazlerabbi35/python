# Python Variable 
"""z = 12
y = '12'
x = 'My name is Fazle Rabbi'

X = 'My name is Radimir'
Z = 19


print(z)
print(Z)
print(type(y))
print(Z)"""


#camelCaseVariable >Except the first word, everything will strat with capital letter.
"""newVariable
firstHeader
newTable"""
#PascalCaseVariable > Each word start with CapitalLetter.
"""ThisIsPascalCaseVariable
FirstTable
SecondTable
NewTable
"""

# Snake_case_variable > each word is separated by underscore character.
"""first_varable
sencond_variable"""


# Multiple variable
"""x, y, z = 'Mango', 9, 'Shirt'
print(x)
print(y)
print(z)"""
"""
fruits = ['Mango', 'Orange', 'Apple']
x, m, a = fruits
print(m + a)
print(a, m)"""

"""
#Global Variable
x = 'awesome'
print(x)

if 10 < 5:
    print(x)
else:
    print('no')"""








"""
# PYTHON DATA TYPES
str > 'Inside quotation, everything will count as a string'
int > 12 , 43, 53
float > 54.4, 53.4
complex > 5j
bool > True"""


"""# type Convesation
a = 43
b = 54.54
c = 5+3j
print(a, b, c)
# x = int(c)
y = float(a)
z = complex(b)
#print(x)
print(y)
print(z)"""





  



##  @@@@@@@@@@@@@@@@@@@@@@  PYTHON STRING  @@@@@@@@@@@@@@@@@@
"""
print('My name is `Fazle Rabbi`.')
print("He is called 'Johnny'.")
print("It's alright.")"""

# multiline String

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# b = """My name is Fazle Rabbi. And I'm originally 
# from Bangladesh."""
# print(b)
"""If we want to take multiple line string, then we need to use 3 quotion mark."""



























"""
# Python Booleans
x = 'Hello'
y = 12
z = ''
Z = ' '
print(bool(Z))
print(bool(z))
print(bool(x))"""



# PYTON Comparison Operator 
"""# there are 6 comparison operator
==  equal
!=  not equal
>  greater than
< less than
>= greater than or equal to 
<= less than or equal to """


# PYTON Arithmetic Operator 
"""# there are 7 arithmetic operator
+ Addition
- subtraction
* multipication
/ Division
% modulus
** exponentiation
// Floor Division """


# PYTON Logical Operator 
"""# there are 3 comparison operator
and
or
not """

# PYTON Bitwise Operator 
"""# there are 6 comparison operator
& and
| or
^ XOR
~ not
  
   
 """








# PYTHON LIST
"""Mylist = ["apple", "Orange", "mango", "Mango", "licci", "apple"]

print(Mylist)
print(Mylist[3])
print(len(Mylist))"""

"""
List_2 = ['String', 12, 43, 'Number', 'Boolenan', True, False]
print(List_2)
print(len(List_2))
print(List_2[-1])
"""

"""ListConstructor = ("ramos", "koros", "messi", "modric")
print(ListConstructor)
new_list = list(ListConstructor)
if "Ronaldo" in new_list:
    print('Yes!, He is on this list.')
else:
    print('No!')
print(new_list)"""


# list, type, access data, change value, add value(append, inser(2))
"""
eleven = ["ramos", "koros", "messi", "modric", "vini", "haland"]

eleven[2:3] = ["foden"]
eleven.insert(4, 'Ronaldo')
print(eleven)"""







##############  IF ELSE
"""a =200
b = 33
c = 43
if b > a:
    print("b is greater than a")
elif a ==b:
    print("a and b are same")
else:
    print("a is greater than b.")
#Short IF
if a > b: print('A is big.')
# Short If Else
print("a is rich") if a == b else print("They are net same.")"""

"""
morning = 10
evening = 6
lesson = "Not Have"
print('Wake up') if lesson == "Have" else print("You can sleep till", morning)"""

"""
x = 54
y = 65
z = 54
if x > y and x > z:
    print('x greater than anything')
elif x < y or y < z:
    print('Z is greater')
else:
    print('Y is greater')"""





# Python While loops
"""i =1
while i < 6:
    print(i)
    i += 1
"""

# Python FOR loops
# BREAK > when it comes to the exact value, it will close counting number.
"""name = 'Fazle Rabbi'
for x in name:
    print(x)
    if x == 'R':
        break"""
# CONTINUE>> IT will count the value except this exact value.
"""list_forLoops = ['bird', 'animal', 'cow', 'fish', 'chicken']
for name in list_forLoops:
    if name == 'cow':
        continue
    print(name)
"""
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) """

"""
for x in range(6):
    print(x)
for y in range (3, 10):
    print(y)
for odd in range(1, 30, 2):
    print(odd)

v = 'BANGLADESH'

for c in v:
    print(c)"""







#### FUNCTION
"""
def my_function(name):
    print("This is my function", name)
my_function("Zebra Function")



v = 'BANGLADESH'
for c in v:
    print(c)

my_function('CROSS')"""

"""
def fruits_fun(name1, name2):
    print(name1, "or", name2, "What wil you choose?")
fruits_fun("Mango", "JackFruits")"""







"""
numbers = [2, 4, 6 ,4, 3, 9, 8, 3,2]

for i in range (len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i], "is a duplicate")
            break;

name = "rabbi"
for k in range (len(name)):
    for n in range(k+1, len(name)):
        if name[k] == name[n]:
            print(name[k]) 
            break;  

basket = ["mango", "lici", "apple", "grapes", "grapes", "lemon", "mango", "lemon"]

for f in range (len(basket)):
    for g in range(f+1, len(basket)):
        if basket[g] == basket[f]:
            print(basket[g] , "is a duplicate")
            break;"""

"""
nam = 'partition'

for n in range(len(nam)):
    for m in range (n+1, len(nam)):
        if nam[m] == nam[n]:
            print(nam[m], 'is a duplicate')
            break;


f = "BANANA"

for k in range(len(f)):
    for l in range(k+1, len(f)):
        if f[l] == f[k]:
            print(f[k], "is a duplicate value")
            break;

for k in f:
    print(k)"""

"""
num = int(input("How many numbers: "))

total_sum = 0
for n in range(num):
    number = float(input("Enter your number: "))
    total_sum += number

avg = total_sum / num
print(avg)"""



