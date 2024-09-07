#list
"""list1 = ["Mango", "Apple", "Cherry"]
print(list1)
list2= list()
print(list2)
# @@ list can allow all data types and duplicates
list3 = [243, 43, "Cherry", True, "Cherry", 34.2, False] 
print(list3)
print(list3[2])
print(list3[-2])

for i in list3:
    print(i)
name = "FazleRabbi"
for n in name:
    print(n)"""
list4 = ["Rafiq", "Sofik", "Jabbar", "Borkot"]
"""for l in list4:
    print(l)
if "Hasina" in list4:
    print("yes")
else:
    print("no")

print(len(list4))  # $ demonstrate the length
list4.append("Rafi") # $ add a new element 
print(list4)

list4.insert(2, "Ronaldo") # $ add a element in a specific location
print(list4)

print(list4.pop()) #$ remove the last element
print(list4)"

print(list4)
ex = list4.remove("Jabbar") # $ the Jabbar element will delete
print(list4)

print(list4)
opposite = list4.reverse()
print(list4)

list5 = ["x", "g", "a", "l", "m", "w", "o", "k", "d"]
print(list5)
list5.sort()
print(list5)
print(list5 * 2) # list cosider everything as a string.
 
list6= [ 0] * 5
print(list6)
list7= [1,2,3,4,5]
print(list7)
print(list6+list7)

list5 = ["x", "g", "a", "l", "m", "w", "o", "k", "d"]
print(list5)
print(list5[3:7])
print(list5[0::2]) # here 0 is the base and 2 is the gap between 2 numbers.
print(list5[-1::-2])

list8 = ["NBA", "Football", "UFC", "Cricket", "Tennis"]

list_cpy = list8.copy() # because of this the original list will be the same.
print(list_cpy)
print(list8)
list_cpy.append("Voleyball")
print(list_cpy)
print(list8)

list_cpy= list(list8)
list_cpy.insert(3, "wressteling")
print(list8)
print(list_cpy)
list9 = [1, 2,3, 4, 5, 6]
m = [n+n for n in list9]
R = [s**s for s in list9]
print(list9)
print(m)
print(R)
"""


#tuples
"""
tuple1 = ("max", 28, "Hunan", "Mango", "toufa", 35, "pifu", "qiangzhuang")
tuple2 = "Unan", "Anhui", 49, "Xia"
tuple3 = ("Nanjing")
print(tuple1)
print(type(tuple1))
print(tuple2)
print(type(tuple2))
print(tuple3)
print(type(tuple3))
print(tuple1[0])
item = tuple2[1:3]
print(item)



for i in tuple2:
    print(i)

if "Una00n" in tuple2:
    print("yes")
else:
    print("no")

for x in tuple1:
    print(x)

if "shenti" in tuple1:
    print("Match!")
elif "shou" in tuple2:
    print("Yes we have")
else:
    print("try next time.")



tuple5 = ("p", "s", "e", "k", "k", "c", "s" ,"l", "l", "q", "k", "k")
print(tuple5)
print(len(tuple5))
print(tuple5.count("k"))
print(tuple5.count("q")) # if it not match it will reply 0.
print(tuple5.index("k"))


list1=list(tuple1)
tuple_l= tuple(list1)
print(tuple1)
print(list1)
print(tuple_l)

tupleA= (1, 2, 3 ,4 ,5, 6, 7, 8, 9, 10, 11, 12, 13)
print(tupleA)
print(tupleA[:5])
print(tupleA[3:])
print(tupleA[4:9])
print(tupleA[2::3])
print(tupleA[12::-1])
"""

#dictionary
"""
dict1= {"name":"Rabbi", "town":"Bogura", "Age":21, "Gender":"Male"}
dict2 = dict(name="saliha", town= "ankara", age=24, gnder="female")
# @@@ add item and delet item
print(dict2)
dict2["club"] = "besiktas"
del dict2["gnder"]
dict2.pop("age")
print(dict2)
print(dict2.popitem())


dict2["email"] = "saliha@gamil.com"
print(dict2)
del dict2["gnder"]
print(dict2)
dict2.pop("age")
print(dict2)


dict1["email"] = "rabbi@xy.com"
print(dict1["Age"])
print(dict2["name"])
print(dict1)
dict1["email"] = "fazle@gmail.com"
print(dict1["email"])
del dict1["email"]
print(dict1)"""




dict3= dict(CB="Ramos",RB="pepe", LB="marcelo",CM = "Kroos", CF="Ronalado")
"""print(dict3)

if "CB" in dict3:
    print(dict3["CM"])

try:
    print(dict3["DM"])
except:
    print(dict3["CM"])
"""
"""
for key in dict3:
    print(key)

for value in dict3.values():
    print( value)
for key in dict3.keys():
    print(key)

for value in dict3:
    print(value)
for key in dict3:
    print(key)

for key in dict3.keys():
    print(key)

for value in dict3.values():
    print(value)
# if you want both key and values in a loop then

for key, value in dict3.items():
    print(key, value)"""

# @@ copy dictionary
"""print(dict3)
dict4 = dict3.copy()
dict4["GK"] = "Iker Casials"
print(dict3)
print(dict4)"""

# @@ update dictionary
"""dict5 = {"Fname": "rabbi", "age": 21, "Mtown": "bogura"}
dict6 = {"Lname": "saliha", "age": 24, "Ftown": "ankara"}

dict5.update(dict6)
print(dict5)"""



#sets
# sets are unordered, mutable, no duplicate
"""
set1 = {1,2,3,4,5,2,4}
print(set1)

set1.add(31)
set1.add(32)
set1.add(33)
set1.add(34)
# @@ they both will delete item form a set.
set1.remove(33)
set1.discard(32)
print(set1)
set1.clear()
print(set1)"""
"""
for i in set1:
    print(i)

if 111 in set1:
    print("yes")
else:
    print("no")"""


a = {1, 2, 4 ,5 ,6, 9, 4,}
b = {0, 2, 3, 7,5, 3, 9, 8, 10}
"""g = a.symmetric_difference(b) # difference betwen them
f = b.difference(a) # differnce that not have in a
e = a.difference(b)
d = a.intersection(b)
c = a.union(b)
print(c)
print(d)
print(e)
print(f)
print(g)"""

# @@ update method for set
"""a.update(b)
print(a)

a.intersection(b)
print(a)
a.intersection_update(b)
print(a)
a.symmetric_difference_update(b)
print(a)

d = a.intersection(b)
print(d)
"""
"""
p = {1, 2, 3, 4, 5}
q = {2, 3, 5}
print(q.issubset(p))

r = {1, 2, 3, 4, 5}
s = {2, 3, 5, 1, 4}
print(r.issubset(s))
print(s.issubset(r))"""



#strings

"""a = "I'm fazle rabbi"
print(a)
b = ""Hello
this is a new one
and there was a little 
more info""
print(b)

s = "     strings strip    "
print(s)
s = s.strip()
print(s)
print(s.upper())
print(s.lower())
print(s.capitalize())
"""




#collections

# collections: Counter, Namedtuple, orderdDict, defaultDict

"""from collections import Counter
a = "xxxyyzzzzmmm"
myCoounter = Counter(a)
print(myCoounter)
print(myCoounter.keys())
print(myCoounter.values())
print(myCoounter.most_common(2))  # it will demonstrate the most common items on the list.
print(list(myCoounter.elements())) # it will demostrate all the item as a list.
"""







#Itertools
# Itertools: product, permutations, combinations, accumaulate, groupby, infinite iterators

"""from itertools import product
a = [1, 2]
b = [5, 6]
prod = product(a, b)
print(list(prod))
"""

"""
from itertools import permutations
a = [1,2,3]
perm = permutations(a, 2) ## 2 is a length of list elements. in permutations it not necessary to use length.
print(list(perm))"""

# difference between permutaions and combinations is permutations allow duplicate while combination doesnot allow any duplicate.
"""
from itertools import combinations
a = [1,2,3]
comb = combinations(a, 2) # 2 is a length of list elements. in combinations we must need to use length.
print(list(comb))
"""

"""from itertools import accumulate
a = [1,2,3,4,5]
accc = accumulate(a)
print(a)
print(list(accc))"""

from itertools import groupby



#Lambda Function
#Exceptions and errors
#Logging
#JSON
#Random Numbers
#Dectators
#Generators
#Threading vs Multiprocessing
#Multithreading
#Multiprocessing
#Function Arguments
#Shallow vs Deep Copying
#The Aesterisk Operator
#Context Managers














#### PYTHON FUNCTION 

# function that will choose specific name in a row
"""def function_2(*name):
    print("This is my boy", name[0])
function_2('Rabbi', 'Radimir', 'Ruo xing')"""



# function that returns the maximum num:
"""def maximum(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    return z
print(maximum(51, 9, 33))"""


# it will give you a sum of a list 
"""def sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(sum((423, 9, 5)))"""

### function that will multiply your numbers
"""def multiply(numbers):
    total = 1
    for i in numbers:
        total *= i

    return total
print(multiply((5, 2, -3, -2)))"""


"""def given_range(n):
    if n in range(3, 9):
        print("%s is in range" % str(n))
    else:
        print("The number is outside the given range")

given_range(56)




def test_range(n):

    for i in range(len(n)):



n = input(int("Enter your pass:"))
test_range()"""


#password = int(input("Enter your pass here: "))
name = "rabbi12345"

counter = 0
for i in name:
    counter += counter
print(str(counter))