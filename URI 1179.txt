# 1179
c=0
odd=[]
even=[]

while c<10:
  a = int(input())


  if a%2==0:
    even.append(a)
  else:
    odd.append(a)
  
  if len(even)==5:
    e=0
    while e<5:
      print('par[%d] = %d'%(e,even[e]))
      e+=1
  if len(odd)==5:
    o=0
    while o<5:
      print('impar[%d] = %d'%(o,odd[o]))
      o+=1
  c+=1
