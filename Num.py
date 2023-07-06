import numpy as np

# ARRAYS: store single data types, efficient than lists, stored in contiguous memory, faster than list
# TYEPES: there are two types of array; vectors & matrices
# VECTORS: one dimensional array
# MATRICES: two or more dimensional array

# COMMON FUNCTIONS
ara = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])  
exit()
print(ara.shape) # defines shape as (row-by-col)
print(np.reshape(5, 2))
print(ara.ndim)  # defines the no. of dimension an array have
print(ara.size)  # defines the no. of entries in an array
print(ara.itemsize) # defines size covered by each item in bytes
print(ara.dtype) # defines data type; customary, we can change it, 
# if dtype is int32 it mean each items cover (4x8) 4 bytes space
print(np.max(ara))    # gives maximum number
print(np.argmax(ara)) # return the index number of highest entity
print(np.argmin(ara)) # # return the index number of lowest entity
print(np.min(ara)) # gives minimum number
print(ara.max(axis=0)) # gives the maximum number along x-axis==axis(0)
print(ara.max(axis=1)) # gives the maximum number along y-axis==axis(1)
print(np.sum(ara))     # summate all numbers; can also use axis here
print(np.prod(ara))    # give the product of all the numbers
print(np.divide(ara, 2)) # gives the divided entries
print(np.subtract(ara, 10)) # gives the subtracted entries through give subtracted value
print(np.arange(20, 49, step=4)) # like python's built-in range function
print(np.linspace(1, 6, 5)) # give the 5 intervally equal number between 1 & 5
print(np.hstack((ara, are))) # horizontall stack arrayys
print(np.vstack((ara, are))) # vertically stack arrsy upon each other
print(np.transpose(ara))
# print(ndarray.flatter(ara))

# STATISTICAL FUNTIONS, we can use axis in these
print(np.mean(ara))
print(np.median(ara))
print(np.percentile(ara, 50))
print(np.var(ara))
print(np.std(ara))
print(np.corrcoef(ara))

#MATHEMATICAL FUNTIONS
print(np.abs(ara))     # return absolute values of entries
print(np.ceil(ara))    # return cieled value like 5.7 --> 5
print(np.floor(ara))   # return floored value like 5.7 -- > 6
print(np.log(ara))     # return natural log of each entries
print(np.log10(ara))
print(np.sin(ara))
print(np.cos(ara))
print(np.tan(ara)) #other funtion: arcsin, arccos, arctan
print(np.sqrt(ara))
print(np.exp(ara))
print(np.round(ara, decimals=2))
print(ara/2)
print(ara*19)
print(ara+ara)
print(ara**ara)
#boolean masking:
print(ara>6)
print(ara==0)
print(ara>4&ara<7)
print(~(ara>4&ara<7))

# SLICING
# mat[row, col] | mat[row][col]
print(ara[0, 0:]) # first row; access element from 0th index to onward 
print(ara[0, :3]) # first row; access element from 0th index to 3rd index
print(ara[0, 2:5])# first row; acces element from 2th index to 4th index
print(ara[:, 4]) # getting element of 5th col
# we can also assign some values to these slice arrays using = operator

# LINEAR ALGEBRA 
print(np.eye(5))    # return unity matrix, takes only shape of matrix
print(np.triu(ara)) # returns upper triangular matrix, takes only given array
print(np.tril(ara)) # returns lower triangular matrix, takes only given array
print(np.zeros(5))  # return null matrix, takes only shape
print(np.full(fill_value=10, shape=(5, 5), dtype=np.int8))  # return matrix with given number
print(np.zeros_like(ara)) # convert any non-zeros array into zero like, takes given array
print(np.full_like(ara, fiil_value=20)) # convert any array into full_like, takes given array
print(np.identity(5)) # return identitiy matrxi takes only squared shape of matrix
print(np.matmul(ara, are)) # do matrix multiplacation
print(np.linalg.det(np.arange(1, 5).reshape(2, 2))) # detereminant of an array
print(np.linalg.inv(ara)) # inverse of given matrix

# LOAD DATA FROM FILE


# MISCELLANEOUS
print(np.equal(ara, are)) # comparing two entries of matrix
