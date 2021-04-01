# 1072

n=int(input())
inn=0
out=0
c=0

while c<n:
    a=int(input())
    if (a>=10) and (a<=20):
        inn+=1
    else:
        out+=1
    c+=1
print("%d in"%inn)
print("%d out"%out)