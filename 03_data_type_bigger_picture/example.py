
# -------------------------------Numbers

a = 12 + 12
print(a)

b = 2.5 * 2
print(b)

import math
print(math.pi)

import random
print(random.random())
print(random.choice([1,2,3,4,5]))

# ---------------------------------String

username = 'helloworld'
print(len(username))
print(username[0]) #just like array or list
# username[0] = 'H'  string is immutable

print(username[-1]) # last character
print(username[1:3]) # el

# dir() method
print(dir(username)) # different method or prop can be used on username

#-----------------------------------List
#list is same as array in js or arraylist in java

mylist = [123, "hello", 3.4]
print(len(mylist)) # count the number of elements --> len() method
print(mylist[0])
print(mylist[-1])


#--------------------------------------Dictionaries

myD = {
    'one' : 'lemon tea',
    'two' : 'ginger tea',
    'superhero' : 'saktiman'
}

print(myD['one'])
print(myD['superhero'])


#-------------------------------------Tuple

myTup = ( 1, 2, 4,3)
print(myTup[0])
print(len(myTup))
