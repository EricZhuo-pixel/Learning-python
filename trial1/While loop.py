#used to repeat a block of code until as long as a condition is true
#we re-check the condition at the end of the loop

name=input('enter your name:')

while name=='':
     name=input('please enter your name:')

age=int(input('enter your age:'))
while age <0:
    age=int(input('please enter a valid age:'))
    print('please enter a valid age:')
print(f'hello {name}')
print(f'you are {age} years old')