#1116
n=int(input())
c=1

while c<=n:
  a,b=map(int,input().split())
  
  if b==0:
    print("divisao impossivel")
  else:
    print("%.1f"%(a/b))
  c+=1