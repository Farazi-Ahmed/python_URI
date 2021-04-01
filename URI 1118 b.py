game=inter=gremio=draw=0

a,b = list(map(int,input().split()))
game+=1
if a>b:
  inter+=1
elif b>a:
  gremio+=1
elif a==b:
  draw+=1
print("Novo grenal (1-sim 2-nao)")

while True:
  c=int(input())
  if c==1:
    a,b = list(map(int,input().split()))
    game+=1
    if a>b:
      inter+=1
    elif b>a:
      gremio+=1
    elif a==b:
      draw+=1
    #print("Novo grenal (1-sim 2-nao)")
  if c==2:
    break
  else:
    print("Novo grenal (1-sim 2-nao)")

print("%d grenais"%game)
print("Inter:%i"%inter)
print("Gremio:%g"%gremio)
print("Empates:%d"%draw)

if inter>gremio:
  print("Inter venceu mais")
elif inter<gremio:
  print("Gremio venceu mais")
elif inter==gremio:
  print("Não houve vencedor")