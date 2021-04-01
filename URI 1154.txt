# 1154
sum=d=0
while True:
  age=int(input())
  if age>0:
    sum+=age
    d+=1
  elif age<0:
    break
print('%.2f'%(sum/d))