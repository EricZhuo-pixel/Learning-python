import numpy as np

rng = np.random.default_rng() #seed reproduces same results every time
#(inclusive, exclusive, size)
print(rng.integers(1, 7, size=3)) # generate 3 random integers between 1 and 6

#2d array
print(rng.integers(1, 7, size=(3,2))) # generate 3 random integers between 1 and 6 in a 3x2 array

np.random.seed() #seed reproduces same results every time

print(np.random.uniform(-1,1,size=(3,2))) # generate 3 random numbers between -1 and 1 in a 3x2 array




random=np.random.default_rng() 
array=np.array([1, 2, 3,4, 5, 6])
random.shuffle(array) #shuffle the array in place
print(array)


poo=np.random.default_rng()
fruit=np.array(['apple', 'banana', 'cherry', 'date', 'elderberry'])
fruit=poo.choice(fruit, size=(3,2))
print(fruit)