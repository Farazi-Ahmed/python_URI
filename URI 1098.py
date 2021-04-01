# 1098 (5% wrong on i = 2)

i = float(0) 
j = float(1)

while i<=2:
  print(i,j)
  if i.is_integer() or j.is_integer():
    print("I={:.0f} J={:.0f}".format(i,j))
    print("I={:.0f} J={:.0f}".format(i,j+1))
    print("I={:.0f} J={:.0f}".format(i,j+2))
  else:
    print("I={} J={}".format(round(i,1),round(j,1)))
    print("I={} J={}".format(round(i,1),round(j+1,1)))
    print("I={} J={}".format(round(i,1),round(j+2,1)))
  i+=round(0.2,1)
  j+=round(0.2,1)