#list[]= mutable, flexible
#tuple()= immutable, faster than list
# set{}= unordered, no duplicates

from turtle import color


fruits=["apple","banana","orange"]


#fruits[0]='grape' #this will change the value of the first element in the list
#fruits.append('grape') #this will add a new element to the end of the list
#fruits.remove('banana') #this will remove the element 'banana' from the list
#fruits.pop() #this will remove the last element from the list
#fruits.clear() #this will remove all elements from the list

for fruit in fruits:
    print(fruit, end=' ')


numbers=(1,2,3,4,5)
#numbers[0]=10 #this will give an error because tuples are immutable
print(numbers[0]) #this will print the first element of the tuple

colors={"red","green","blue"}
colors.add("yellow") #this will add a new element to the set
colors.remove("green") #this will remove the element 'green' from the set
#colors.clear() #this will remove all elements from the set
print(colors) #this will print the updated set of colors
color=input("enter a color:")

if color in colors:
    print(f"{color} is in the set of colors")
else:
    print(f"{color} is not in the set of colors")