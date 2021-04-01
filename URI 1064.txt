# 1064

d=0
c=1
sum=0
while c<=6:
    a=float(input())
    if a>0:
        d+=1
        sum+=a
    c+=1
print("%d valores positivos"%d)
print("%0.1f"%(sum/d))