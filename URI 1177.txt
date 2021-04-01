# 1177
t=int(input())
d=0
limit=1000
while d<limit:
  c=0
  while c<t:
    print('N[{}] = {}'.format(d,c))
    c+=1
    d+=1
    if d==limit:
      break