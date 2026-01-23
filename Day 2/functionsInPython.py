# Basic function 
def sayHello():
    print("Hello")

sayHello()

# Function with one parameter
def greet(name):
    print("Hello",name)

greet("Harshit")
greet("Sahil")

# Function with multiple parameter

def add(a,b):
    print(a+b)

add(3,5)
add(3,9)

# Function returning value

def add(a,b):
    return a + b

print(add(3,19))

# Function with default values 

def greet(name = "friend"):
    print("Hello",name)

greet()
greet("Harshit")