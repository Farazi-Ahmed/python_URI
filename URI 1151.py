# 1151
n=int(input())
if n==1:
  a=0
  print(a,end=" ")

if n==2:
  b=1
  print(b,end=" ")

if n==3:
  x=a+b
  print(x,end=" ")

if n==4:
  y=b+x
  print(y,end=" ")

c=4
while c<n:
  z=x+y
  print(z,end=" ")
  if n==5:
    break
  x=z+y
  print(x,end=" ")
  if n==6:
    break
  y=x+z
  print(y,end=" ")
  if n==7:
    break
  c+=3