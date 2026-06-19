#evaluates multiple conditions 
#or=at least one condition must be true
#and=all conditions must be true
#not=negates a condition

temp=25
is_raining=False
if temp > 20 and temp <30 and not is_raining:
    print('the event is on')
else:
    print('the event is cancelled')