# 1164
n=int(input())
c=1
while c<=n:
  a=int(input())
  sum=0
  d=1
  x=0
  while d<a:
    if a%d==0:
      sum+=d
    d+=1
  if sum==a:
    print('%d eh perfeito'%a)
  else:
    print('%d nao eh perfeito'%a)
  c+=1