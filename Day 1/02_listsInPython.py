# List in python
nums = [12,25,6,13]
print(nums)
print(nums[0])
print(nums[2:])
print(nums[-1])
print(nums[-4])
print(nums[1:5:2])

# string List
names = ["Ram","Shyam","Raju"]
print(names)

# List with diff data types
values = [9.5,7,'Ram']
print(values)

# List of List
nil = [nums, names]
print(nil)

# List are mutables
# List operations : -

# 1 - append add the value in the last of existing list
nums.append(45)
print(nums)

# 2 - insert the element at the given index
nums.insert(2,78)
print(nums)

# 3 - remove the element from the list by passing its value
nums.remove(12)
print(nums)

# 4 - Find minimum element of the list
print("Minimum value of the list is: ",min(nums))

# 5 - Sort method is used to sort the current list
nums.sort()
print("Sorted list: ",nums)

# 6 - pop with index is used to remove the value from tha position
nums.pop(1) 
print("Value removed from index 1: ",nums)

# 7 - normal pop method will remove a value from the end
nums.pop() 
print("After popping: ",nums)

# 8 - del is used to delete the elements of list from the given index
del nums[2:]
print("After deletion: ",nums)

# 9 - extends used to add values in the list from the last
nums.extend([29,12,14,36])
print("Extended elements are: ",nums)

# 10 - max will return the maximum value of the list
print("Maximum value of the list is: ",max( nums))

# 11 - sum will return the sum of elements in the array
print("Sum of the elements is: ",sum(nums))

