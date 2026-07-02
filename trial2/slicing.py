import numpy as np

array=np.array([['a', 'b', 'c'],
             ['d', 'e', 'f'],
            ['g', 'h', 'i'],
          ['j', 'k', 'l']])

# array[start:end:step]

#print(array[0]) show the first row of the array
#print(array[0:3]) #show the first three rows of the array
#print(array[0:4:2]) #show the first four rows of the array with a step of 2
#print(array[::-1]) #show the array in reverse order
#print(array[:,0]) #show the first row and first column of the array

print(array[:,1:4]) #show the first row and first column of the array
