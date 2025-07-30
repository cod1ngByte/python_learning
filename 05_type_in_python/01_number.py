
x = 2
y = 3
z = 5
print(x+y)

print( 40 + 2.5)

#print('python' + 2) # error can only concatenate str not int
print('python' + "2") 

print( int ( 2.5)) # 2
print(float(40)) # 40.0
print('hello '+ 'world')
print(x,y,z)
print(x ** 2)

print( 100 ** 2)
print( 2 ** 100)
#python can handle very large number easily, unlike other programming languages
#print( 2 ** 10000)


# True and False is treated as 1 and 0

print( 1 < 2) # True
print( 5 != 5) # False
print( 4 != 5) # True

x = 2
y = 3
z = 4

print( x < y < z) 
# same as
print( x < y and y < z) #True

print( 1 == 2 < 3)
#same as
print( 1 == 2 and 2 < 3) #False


##--------------------------------------------------------------------
import math
print(math.floor( 3.5)) #3
print(math.floor( 3.7)) #3
print(math.floor( 3.2)) #3

print(math.ceil(3.2)) #4
print(math.ceil(3.5)) #4
print(math.ceil(3.7)) #4


#trunc() will give the result towards zero on number line
print(math.trunc(3.5)) #3
print(math.trunc(3.2)) #3
print(math.trunc(2.7)) #2
print(math.trunc(-3.7)) #-3


#----------------------------------------------------------------------------------------
#octa, hexa and binary
# return the decimal value

print(0o20) # 16
print(0xFF) # 255
print(0b1000) # 8


#takes decimal value return octa or hexa or binary
print(oct(16)) # 0o20
print(hex(255)) # 0xff
print(bin(8)) # 0b1000


#----------------------------------------------------------------------------------
import random

print(random.random()) # random number between (0,1)
print(random.randint(2,5)) # random number between [2,5]
print(random.randint(1,6))

l1 = ['lemon', 'masala', 'ginger','honey']
# choice method take list as an argument
print(random.choice(l1))

print(l1)
print(random.shuffle(l1))
print(l1)