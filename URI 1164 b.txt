# 1164
n=int(input())
c=1
while c<=n:
  a=int(input())
  sum=0
  d=1
  x=0
  while d<=a:
    if a%d==0:
      x+=1
    d+=1
  if x==2:
    print('%d eh primo'%a)
  else:
    print('%d nao eh primo'%a)
  c+=1