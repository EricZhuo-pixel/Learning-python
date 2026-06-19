#typecasting

name="" 
age=15
gpa=5.9
is_students=True

print(type(name))

gpa=int(gpa)
print(gpa)

age=float(age)
print(age)

age=str(age)
print(type(age))
#str makes it so it adds on unlike addition if used +=1
#then the print would be 151 and not 16

name=bool(name)
print(name)