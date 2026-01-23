# Dictonary in python
data = {1:"harshit",2:"sahil",3:"siddhesh"}
print(data)

# Fetching the dictonary values using key
print(data[1])

# we can fetch the value using get method
print(data.get(1))

# It will not throw an error even if the key value is not present
print(data.get(4))

# we can use a alternative to avaoid getting nothin in output
print(data.get(1),'Data Not found')

# Converting two different list into dict
values = ["Python","Java","JS"]
key = ["Harshit","Sahil","Sid"]
data = dict(zip(key,values))
print(data)

# Adding new value in dictonary
data['Riya'] = 'C#'
print(data)

# Deleting the values from the dictonary
del data['Riya']
print(data)
