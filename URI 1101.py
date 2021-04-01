# 1101

a,b = map(int, input().split())

while (a>0) and (b>0):
    if b<a:
        t1 = a
        a = b
        b = t1
    sum=0
    while a<=b:
        sum+=a
        print(a,end=" ")
        a+=1
    print("Sum=%d"%sum)
    a,b = map(int, input().split())