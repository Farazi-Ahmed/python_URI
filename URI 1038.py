#1038

value=input().split(" ")
x,y = value
z=0

if int(x) == 1: 
  z = 4
elif int(x) == 2: 
  z = 4.5
elif int(x) == 3: 
  z = 5
elif int(x) == 4: 
  z = 2
elif int(x) == 5: 
  z = 1.5
else:
  z = 0

bill=float(z)*int(y)

print("Total: R$ %.2f"%bill)