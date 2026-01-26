import numpy as np
list1 = [1,2,3,4,5]
#print(list1)
#print(list1[0])

list2 = ["Jhon elder",41,list1,True]
#print(list2)

# Numpy - Numeric python
# ndarray = n-dimensional array

np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

np2 = np.arange(10)
print(np2)

np3 = np.arange(0,10,2)
print(np3)

np4 = np.zeros(10)
print(np4)

np5 = np.zeros((2,10))
print(np5)

np6 = np.full((10),6)
print(np6)

np7 = np.full((2,10),6)
print(np7)

my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8)

x = np.array([1,2,3])
y = x * 2
print(y)
z = x + 10
print(z)


print("Operation on scores numpy array")
scores = np.array([80,90,78])
print(scores.mean())    
print(scores.sum())
print(scores.max())
print(scores.argmax())
print(scores.argmin())
print(np.sqrt(scores))