# 1099
n = int(input())
c = 1

while c<=n:
    sum=0
    a,b = map(int,input().split(" "))

    if b<a:
        t1 = a
        a = b
        b = t1
    
    a = a + 1
    while a<b:
      if a%2!=0:
          sum+=a
      a+=1

    if sum!=0:
      print(sum)
    else:
      print(0)
    c+=1