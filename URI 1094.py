# 1094

n = int(input())
c=r=s=0
csum = rsum = ssum = 0
a=0

while a<n:
  
    num,type1 = input().split()
    num = int(num)
    
    if type1=="C":
        c+=1
        csum+=num
    elif type1=="R":
        r+=1
        rsum+=num
    elif type1=="S":
        s+=1
        ssum+=num
    a+=1
    
total= csum+rsum+ssum

print("Total: %d cobaias"%total)
print("Total de coelhos: %d"%csum)
print("Total de ratos: %d"%rsum)
print("Total de sapos: %d"%ssum)
print("Percentual de coelhos: {:.2f} %".format((csum/total)*100))
print("Percentual de ratos: {:.2f} %".format((rsum/total)*100))
print("Percentual de sapos: {:.2f} %".format((ssum/total)*100))