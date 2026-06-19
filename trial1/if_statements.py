#execute some sode only if a coniditon is true

age=int(input('enter your age:'))
has_ticket=True
price=15



if age >=65:
    print('you are a senior citizen')

elif age >= 18:
    print('you are an adult')
    print(f'the price is ${price}')
#basic decision making
#elif=else if 
elif age <0:
    print('you are not born yet')
elif age==0:
    print('you are a newborn')
else:
    print('you are a child')
    price=int(price/2)
    print(f'the price is ${price}') #or print(f'the price is ${price*0.5}')


if has_ticket:
    print('you can enter the movie')
else:
    print('you cannot enter the movie')