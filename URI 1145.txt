# 1145

x,y=map(int,input().split())

c=1
while c<=y:
  print(c,end=" ")
  if c%x==0:
    print(" ")
  c+=1