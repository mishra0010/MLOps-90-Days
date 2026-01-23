# Basic Lambda structur
add = lambda a,b:a+b
print(add(2,3))

# Single paramter Lambda
square = lambda num:num*num
print(square(2))

# Lambda with condition
check_even = lambda n: "Even" if n%2 == 0 else "Odd"
print(check_even(10))
print(check_even(17))

# Lambda without storing 
print((lambda x:x*3)(4))

# Lambda with map() Every where
numbers = [1,2,3,4]
squares = list(map(lambda x:x*x,numbers))
print(squares)

# Lambda with filter()
evens = list(filter(lambda x:x%2 == 0, numbers))
print(evens)