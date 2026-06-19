age=int(input('enter your age:'))
partner_age=int(input('enter your partner age:'))
if age >=18 and partner_age >=18:
    print('You and your partner are of age')

elif (age <0 or age==0) and (partner_age <0 or partner_age==0):
    print('neither you nor your partner is born yet')

elif (age <=18 ) and partner_age <=18:
    print('you and your partner are together')
else:
    print('you and your partner are not supposed to be together')