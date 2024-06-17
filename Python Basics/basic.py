import random
# python is dynamically typed language : no need to explicitly specify data type of variable
a = 5
b = 1.2
c = 'a'
d = "python"
#to print we can use just a print statement
print(a) 
print(a, b, c, d) #to print multiple statements using single statement 
# comments in python are written using "#" symbol
# python does not support multiline comments
"""
hii my name is rohan 
this is multiline comment
"""
# data types in python
# 1. Numeric : int, float, complex
a=1
print(type(a))
b=1.2
print(b)
print(type(b))
b = int(b)
print(b)
print(type(b))
c= 3+2j
print(type(c))

randomNum = random.randrange(0,10)
print(randomNum)

# 2. string
str = "ABCD"
char = 'a'

print("A" in str)
print("length of string","'",str,"'",len(str))
multiLine = '''to print multiple statements using single statement, 
comments in python are written using symbol
python does not support multiline comments'''
print(multiLine)

txt = "I am very excited"
if "am" in txt:
    print('yes,"am" is present in txt')
# 3. Boolean
res = True
print(type(res))

# slicing the text
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(text[10:25])
print(text[:25])
print(text[10:])
print(text[:])
print(text[::-1])


text2 = "RoHAn kAdAM"
print(text2.upper())
print(text2.lower())
print(text2.capitalize())

text3 = "Hii, Rohan Here"
print(text3.strip())
print(text3.split(","))

t1 = "Hello"
t2 = " World !"
t3 = t1+t2
print(t3)

age = 22
intro = "My age is ", age

# formatted strings
price = 100
t4 = f"the price is ${price}"
print(t4)

# 4. list
li = ['A',2,"abc",True,1.234]
print(li)


# 5. dict
dict1 = {"name": "rohan","age" : 19,"location": "pune"}
print(dict1)

# 6. tuple
tuple1 = (1,"abc",2.34,False)
print(tuple1)

# 7. set
set1 = {1,2,3,4,5,10}
print(set1)

# 8. range
r = range(6)
print(r)
for i in r:
    print(i)

# conditional statements in python
# if statement
if 5>2:
    print ("true")

# if-else loop
if 2==2:
    print ("true")
else:
    print ("false")

# if-elif-else nested statements
a = 10
b = 12
c = 24
if a>b and a>c:
    print(a,"is maximum")
elif b>c:
    print(b,"b is maximum")
else:
    print (c,"c is maximum")

# Loops
# 1. for loop
"""
for i in range (1,11):
    print(i*4)

"""

