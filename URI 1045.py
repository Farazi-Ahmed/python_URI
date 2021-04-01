# 1045
a,b,c=list(map(float,input().split()))

if (b>a):
  t1=a
  a=b
  b=t1
if (c>a):
  t2=a
  a=c
  c=t2
if (c>b):
  t3=b
  b=c
  c=t3

if (a>=(b+c)):
    print("NAO FORMA TRIANGULO")
elif (a*a)==((b*b)+(c*c)):
    print("TRIANGULO RETANGULO")
elif (a*a)>((b*b)+(c*c)):
    print("TRIANGULO OBTUSANGULO")
elif (a*a)<((b*b)+(c*c)):
    print("TRIANGULO ACUTANGULO")
if (a==b) and (b==c):
    print("TRIANGULO EQUILATERO")
elif (a==b or b==c):
    print("TRIANGULO ISOSCELES")