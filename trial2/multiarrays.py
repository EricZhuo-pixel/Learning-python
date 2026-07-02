import numpy as np

#1,2,3,4,5 dimentional (stopped at 3)
#array=np.array(['a', 'b', 'c'])

#array=np.array([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])

array=np.array([[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']],
                [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', '_']]])



#print(array.ndim)
#print(array.shape)   shows the layers rows and columns of the array
#print(array[0, 1, 2])   #shows the first layer, second row, third column

word=array[0, 1, 2] + array[1, 1, 2] + array[2, 1, 2]
print(word)