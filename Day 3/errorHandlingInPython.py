# x = 10 / 0 -- It will throw zero division error

# Basic value error
try:
     x = int("abc")
except ValueError:
     print("That was not a number")

# Catching errors with multiple except blocks
try:
     x = int(input("Enter a number: "))
     y = 10/x
except ValueError:
     print("You must enter a number")
except ZeroDivisionError:
     print("You cannot divide by zero")

# Catching multiple exception at once
try:
     x = int(input("Enter a number: "))
     y = 10 / x
except(ValueError,ZeroDivisionError):
     print("Invalid input")

# Trying with else

try:
     x = int("10")
except ValueError:
     print("Conversion failed")
else:
     print(type(x))

# Finally block always run example
try:
     file = open("data.txt")
     data = file.read()
except FileNotFoundError:
     print("File not found")
finally:
    #  file.close()
     print("Exiting")


# Raising our own exceptions
def withdraw(balance,amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount

try:
     withdraw(100,200)
except ValueError as e:
     print(e)