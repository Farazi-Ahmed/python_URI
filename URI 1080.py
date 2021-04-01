# 1080

max=0
d=0
c=0

while c<2:
    a=int(input())
    if a>=max:
        max = a
        d = c+1
    c+=1
print(max)
print(d)