# 1158
n=int(input())
c=1
while c<=n:
  d=0
  a,b=map(int,input().split())
  if a%2!=0:
    d=a
  elif a%2==0:
    d=(a+1)

  sum=0
  x=1
  while x<=b:
    sum+=d
    d+=2
    x+=1
  print(sum)
  c+=1