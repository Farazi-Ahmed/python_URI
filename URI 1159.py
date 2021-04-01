# 1159
while True:
  n=int(input())
  if n!=0:
    sum=d=0
    if n%2==0:
      d=n
    elif n%2!=0:
      d=(n+1)
    
    c=1
    while c<=5:
      sum+=d
      d+=2
      c+=1
    print(sum)
  if n==0:
    break