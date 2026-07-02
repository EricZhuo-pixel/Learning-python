import numpy as np

#process of selecting elements that match a certain condition

ages=np.array([[10, 14, 34, 74, 23, 63, 13, 45], [54,23, 14, 17, 65,52,15,63]])


teenagers =ages[ages<18]
adults=ages[(ages>=18) & (ages<65)]
elders=ages[ages>=65]
even=ages[ages%2==0]
odds=ages[ages%2!=0]
print(teenagers)
print(adults)
print(elders)
print(even)
print(odds)


adultss=np.where(ages >= 18, ages, 0)
print(adultss)

