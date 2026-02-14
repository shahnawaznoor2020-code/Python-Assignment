import math
number = int(input("Enter a positive number: "))
e_value=math.e
sqrt=math.sqrt(number)
logarithm = math.log(number,e_value)
sine_function = math.sin(number)

print(f"The square root of {number} is {sqrt}")
print(f"The logarithm of {number} is {logarithm}")
print(f"The sine of {number} is {sine_function}")