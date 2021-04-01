# 1175
l=[]
c=0
while c<20:
  a=int(input())
  l.append(a)
  c+=1

d=(20-1)
while d>=0:
  print('N[{}] = {}'.format(c-20,l[d]))
  a+=1
  c+=1
  d-=1