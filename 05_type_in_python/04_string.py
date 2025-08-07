
str = 'Lemon Chai'
print(str)
print(len(str)) # length of string is 10 (# of charcter (space is also a character))


# extracting character -> string is treated like a list
print(str[0]) #L
print(str[8]) #a


#slicing 
print(str[0:6]) # last index is not included --> #Lemon -> new string is returned
print(str) # no changes in original string, string is immutable


str = '0123456789'
print(str)
print(len(str))#10
print(str[:]) # 0123456789 --> entire string
print(str[4:]) # 456789 --> 4th index till end
print(str[:8]) # 01234567 -> last index is not inlcuded
print(str[0:7:2]) # 0246 --> hop count is 2
print(str[0:7:3]) # 036 --> hop count is 3
print(str) # 0123456789--> no changes on original string, string is immutable


#common method on string
str = "Masala Chai"

#lower() and upper()
print(str.lower()) #"masala chai"
print(str.upper()) #" MASALA CHAI"

#find()
print(str.find("Chai")) # 7 -->return index if found 
print(str.find("chai")) # -1 --> return -1 if no found
print(str) # Masala Chai-->string are immutable, no changes on original string

#strip()
str1 = '  Lemon Chai   '
print(str1.strip()) #Lemon Chai --> remove leading and trailing spaces
print(str1) #  Lemon Chai   --> no changes on original string

#replace()
str2 = "Lemon Chai"
print(str2.replace('Lemon','Masala')) # Masala Chai
print(str2)# Lemon Chai --> no changes

#count()
str3 = "Black Coffee Coffee Coffee"
print(str3.count('Coffee')) # 3 --> return #f of count of given argument

#placeholder
coffee_type = "Black"
quantity = 2
order = "I ordered {} cup of {} coffee"
print(order.format(quantity,coffee_type)) # I ordered 2 cup of black coffee

#split() --> string into list
str = "Expresso, Cappuccino, Lattes, Cold Brew"
print(str.split(", ")) # ['Expresso', 'Cappuccino', 'Lattes', 'Cold Brew'] -->return list
print(str) # Expresso, Cappuccino, Lattes, Cold Brew --> no changes

#join() --> list into string
l1 = ['Expresso', 'Cappuccino', 'Lattes', 'Cold Brew']
print(", ".join(l1)) # Expresso, Cappuccino, Lattes, Cold Brew --> return string
print(l1)


#extracting character from string using for loop
str = "Expresso, Cappuccino, Lattes, Cold Brew"
for charct in str:
    print(charct)

#check if string or charcter is on given string or not
str = "lemon chai"
print("lemon" in str) # True
print("Lemon" in str) # False


#print method
str = "Lemon\n chai"
print(str) # Lemon and chai in next line because of \n escape sequence

str = r"Lemon\n chai"
print(str) # Lemon\n chai --> print as it is