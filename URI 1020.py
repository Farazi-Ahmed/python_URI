#1020

age=int(input())

yrs=months=days=num=0
num=age

while age!=0:
    if age>=365:
        yrs=age//365
        age=age%365
    elif age>=30:
        months=age//30
        age=age%30
    else:
        days=age
        age=0
print(age)
print("%i ano(s)"%yrs)
print("%i mes(es)"%months)
print("%i dia(s)"%days)