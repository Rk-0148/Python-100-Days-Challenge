# This is a comment in Python

# Variables
name = "Alice"
age = 25
height = 5.6  # height in feet

# Printing statements
print("Hello, world!")
print("Name:", name)
print("Age:", age)
print("Height:", height)

# Arithmetic operations
a = 10
b = 3

sum_result = a + b
difference_result = a - b
product_result = a * b
division_result = a / b
modulus_result = a % b

# Printing the results of arithmetic operations
print("Sum of", a, "and", b, "is:", sum_result)
print("Difference of", a, "and", b, "is:", difference_result)
print("Product of", a, "and", b, "is:", product_result)
print("Division of", a, "by", b, "is:", division_result)
print("Modulus of", a, "and", b, "is:", modulus_result)

# Using formatted strings for printing
print(f"{name} is {age} years old and {height} feet tall.")

# Basic if-else statement
if age > 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is not an adult.")

# Loop: Printing numbers from 1 to 5
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)
