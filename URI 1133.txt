# 1133

x = int(input())
y = int(input())

if x>y:
  t1=x
  x=y
  y=t1
  
c=x+1
while c<y:
  if (c%5==2) or (c%5==3):
    print(c)
  c+=1