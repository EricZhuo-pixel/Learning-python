#for loop =used to repeat a block of code a specific number of times(string, list, tuple, set)

name='eric'


for i in range(1,11,2):
    print(i)

for letter in name:
    print(letter,end='-')

import time

for e in range(10,0,-1):
    print(e)
    time.sleep(1)
    
print('blast off!')