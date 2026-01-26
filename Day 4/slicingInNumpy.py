import numpy as np

# Slicing the numpy array
np1 = np.array([1,2,3,4,5,6,7,8,9])

# Return 2,3,4,5
print(np1[1:5])

# Return from something till the end of the array!
print(np1[3:])

# Return negative slices
# 7 8 
print(np1[-3:-1])

