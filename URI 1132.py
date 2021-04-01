# 1132

x = int(input())
y = int(input())

if x>y:
  t1=x
  x=y
  y=t1

sum=0
c=x
while c<=y:
  if c%13==0:
    pass
  else:
    sum+=c
  c+=1
print(sum)