# 1180
n=int(input())
lista = list(map(int,input().split()))
m=lista[0]
d=0
c=0
count=0
for i in lista:
 # print(i,d,m)
  if i<m:
    m=i
    d=count
    #print(m,d)
  count+=1
print('Menor valor: %d'%m)
print('Posicao: %d'%d)