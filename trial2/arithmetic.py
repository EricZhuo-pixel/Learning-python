import numpy as np

# scaler arithmetic


array=np.array([1, 2, 3])

#print(array+1)
#print(array-1)
#print(array*2)
#print(array/2)
#print(array**2) 



#vectorized math functons

#print(np.sqrt(array))
#print(np.round(array)) 
#print(np.floor(array))
#print(np.ceil(array))


#exercise
radii=np.array([1, 2, 3])

print(np.pi* radii **2)


#element wise arithmetic

array1=np.array([1, 2, 3])
array2=np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)

#comparison operators
scores=np.array([90, 80, 70, 60, 50])
print(scores >= 70)

scores[scores >= 70]= 100
print(scores)