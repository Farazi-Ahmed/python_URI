# 1143

n=int(input())
c=1
d=1
while d<=n:
  if c<=n:
    print(c,end=" ")
    print(c*c,end=" ")
    print(c*c*c)
  else:
    d+=1
  c+=1