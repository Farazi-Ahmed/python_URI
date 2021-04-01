# 1172
c=0
x=[]
while c<10:
  a=int(input())
  if a>0:
    x.append(a)
    print('X[{}] = {}'.format(c,a))
  else:
    x.append(1)
    print('X[{}] = {}'.format(c,1))
  c+=1