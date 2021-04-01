# 1134
print("MUITO OBRIGADO")
alcohol=gasoline=diesel=0
while True:
  a=int(input())
  if a==1:
    alcohol+=1
  elif a==2:
    gasoline+=1
  elif a==3:
    diesel+=1
  elif a==4:
    break
print("Alcool: %a"%alcohol)
print("Gasolina: %g"%gasoline)
print("Diesel: %d"%diesel)