import random

number = int(input("number >>>"))

def randomizeList(list):
    list2 = []
    while(len(list) > 1):
        r = random.randrange(0, len(list))
        list2.append(list[r])
        list.pop(r)
    list2.append(list[0])
    return list2

def genList(var):
    list3 = []
    while(var != 0):
        list3.append(var)
        var -= 1
    return list3

set = genList(number)
print (set)
set = randomizeList(set)
print ("")
print ("")
print ("")
print (set)
