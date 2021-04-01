#1117
c=1
sum=0

while c<=2:
    a=float(input())
    if (a>=0) and (a<=10):
        sum+=a
        c+=1
    else:
        print("nota invalida")
print("media = %.2f"%(sum/2))