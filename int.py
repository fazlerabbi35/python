list1 = ["Ramos",4, "Pepe",3,  "Marcelo", 12, "Casemiro", 14, "Carvajal",2,  "Nacho"]

#print(list1)
#print(list1[5:])
#print(list1[-1])
#print(list1[3::2])
"""print(list1[-3])
print(list1[-1:])
print(list1[-1:-5])
print(list1)
item2 = list1[-1:-5]
print(item2)"""
"""for p in list1:
    print(p)

for r in list1:
    print(r)

if "Varane" in list1:
    print("It's found!")
else:
    print("Not Found!")"""
"""
print(len(list1))
print(list1)
list1.append("Varane")
print(list1)
list1.insert(-1, 5)
print(list1)

print(list1)
print(len(list1))
list1.insert(5, "Rudiger")
print(list1)
print(list1)
list1.pop()
print(list1)
list1.remove("Marcelo")
print(list1)

print(list1)
list1.remove(12)
print(list1)"""
# apend, insert, pop, remove;
"""print(list1)
list1.reverse()
print(list1)"""

list2 = [1, 2, 3, 4, 5, 6, 7]
"""print(list2 * 2)
#print(list2 ** 2)
#print(list2 * list2)
print(list2 + list2)

M = [m * m for m in list2]
N = [n ** n for n in list2]
O = [o + o for o in list2]
print(M)
print(N)
print(O)"""

"""
print(list2)

list_cpy = list2.copy()
list_cpy.append("New")
print(list2)
print(list_cpy)

list_cpy2 = list(list2)
list_cpy2.insert(3, "Mango")
print(list_cpy2)
print(list2)
print(list_cpy)"""

from collections import Counter

my_name = "Fazle Rabbi"
my_counter = Counter(my_name)
"""print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2))
print(list(my_counter.elements()))

she = "SalihaSahin"
her = Counter(she)
print(her)
print(her.most_common(3))


tweleve = "Romero"
PT = Counter(tweleve)
print(PT)
print(PT.keys())
print(PT.most_common())"""

"""
i = 10
while i < 15:
    print(i)
    i += 1;
"""
"""
i = 1
while i <7:
    print(i)
    if i == 3:
        break
    i += 1;"""
"""
i = 1
while i < 9:
    i += 1
    if i == 5:
        continue
    print(i)"""

"""
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("i is no longer than 6")"""


"""
n = 1
while n < 4:
    print(n)
    if n == 2:
        break
    n += 1;

m = 1
while m < 8:
    m += 1
    if m == 6:
        continue
    print(m)"""

"""for i in range(1, 9):
    print(i)

fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)
name = 'rabbi'
for n in name:
    print(n)"""

"""
fruits = ["apple", "banana", "cherry", "grapes"]
for f in fruits:
    print(f)
    if f =="cherry":
        break
    
fruits = ["mango", "licci", "orange", "melon"]
for k in fruits:
    if k == "licci":
        break
    print(k)

striker = ["Ronaldo", "Messi", "Neymar", "Mbappe"]
for s in striker:
    print(s)
    if s == "Neymar":
        break


midfilder = ["Modric", "Kross", "Ozil", "Valvarde", "Kevin"]
for m in midfilder:
    if m == "Ozil":
        continue
    print(m)
"""
"""
for x in range(6):
    print(x)
for y in range(1, 9):
    print(y)
for z in range (21, 39, 4):
    print(z)"""

"""midfilder = ["Modric", "Kross", "Ozil", "Valvarde", "Kevin"]
number = [10, 8, 11, 18, 17]

for n in number:
    for m in midfilder:
        print(n, m)
"""

### DUPLICATE DITACTOR
"""name = "Inheritance"

for n in range(len(name)):
    for m in range(n +1 ,len(name)):
        if name[n] == name[m]:
            print(name[m], " is a duplicate value.")
            break
"""