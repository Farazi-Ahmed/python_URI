# 1018

value=int(input())

hundred = fifty = twenty = ten = five = two = one = num = 0
num = value
while value!=0:
    if value>=100:
        hundred = value//100
        value = value%100
    elif value>=50:
        fifty = value//50
        value = value%50
    elif value>=20:
        twenty = value//20
        value = value%20
    elif value>=10:
        ten = value//10
        value = value%10
    elif value>=5:
        five = value//5
        value = value%5
    elif value>=2:
        two = value//2
        value = value%2
    else:
        one=value
        value=0
        
print(num)
print("%d nota(s) de R$ 100,00"%hundred)
print("%d nota(s) de R$ 50,00"%fifty)
print("%d nota(s) de R$ 20,00"%twenty)
print("%d nota(s) de R$ 10,00"%ten)
print("%d nota(s) de R$ 5,00"%five)
print("%d nota(s) de R$ 2,00"%two)
print("%d nota(s) de R$ 1,00"%one)