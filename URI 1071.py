# 1071

x=int(input())
y=int(input())
sum=0

if x<y:
    t1=x
    x=y
    y=t1

while y<(x-1):
  y+=1
  if y%2!=0:
    sum+=y
  
print(sum)