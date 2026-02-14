def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

number = int(input("Enter a number: "))
factorial = fact(number)
print(f"Factorial of {number} is {factorial}")