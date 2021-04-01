# 1150
x=int(input())

while True:
  z = int(input())
  if z>x:
    sum=x
    d=1
    c=1
    while sum<z:
      sum=sum+(x+c)
      d+=1
      c+=1
    break
print(d)