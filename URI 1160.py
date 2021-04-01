# 1160
n=int(input())

x=1
while x<=n:
  a,b,c,d = input().split()
  a = int(a)
  b = int(b)
  c = float(c)
  d = float(d)
  

  if a>b:
    t1=a
    a=b
    b=t1
  if c<d:
    t2=c
    c=d
    d=t2

  t=0
  y=0
  while y<=100:
    start=round(a*(1+(c/100))**y,0)
    start2 = int(start)
    end = round(b*(1+(d/100))**y,0)
    end2 = int(end)

    if start2>end2:
      t+=1
    if t==1 or (t==1 and y<=100):
      print('%d anos.'%y)  
    
    y+=1
    if y>100:
      print("Mais de 1 seculo.")

  x+=1