# 1142

n=int(input())
c=1
d=1
while d<=n:
  if c%4!=0:
    print(c,end=" ")
  else:
    print("PUM")
    d+=1
  c+=1