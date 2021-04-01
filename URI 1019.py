# 1019

N=int(input())
hours=mins=sec=num=0
num=N

while N!=0:
    if N>=3600:
        hours=N//3600
        N=N%3600
    elif N>=60:
        mins=N//60
        N=N%60
    else:
        sec=N
        N=0
print(str(hours)+":"+str(mins)+":"+str(sec))