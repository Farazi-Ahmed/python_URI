# 1118

x=1
sum=0
while x<=2:
    n = float(input())
    if n<0 or n>10:
      print("nota invalida")
    else:
      sum+=n
      x+=1

print("media = %.2f"%(sum/2))
print("novo calculo (1-sim 2-nao)")

d=1
while d==True:
  x=int(input())
  if x==1:
    c=1
    sum2=0
    while c<=2:
      t = float(input())
      if t<0 or t>10:
        print("nota invalida")
      else:
        sum2+=t
        c+=1
    #d+=1
    print("media = %.2f"%(sum2/2))
  if x==2:
      break
  elif x!=1 or x!=2:
    print("novo calculo (1-sim 2-nao)")