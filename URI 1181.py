# 1181
l = int(input())
if l>=0 and l<=11:
  a=input()
  if a=='S':
    c=0
    sum=0
    while c<=11:
      s=float(input())
      sum+=s
      c+=1
    print('%.1f'%sum)

  elif a=='M':
    c=0
    sum=0
    while c<=11:
      s=float(input())
      sum+=s
      c+=1
    print('%.1f'%(sum/12))