# 1051

a = float(input())

if a>=0.00 and a<=2000:
    print("Isento")
elif a>=2000.01 and a<= 3000:
    tax = (a-2000)*0.08
    print("R$ %.2f"%tax)
elif a>=3000.01 and a<=4500:
    tax=(1000*0.08)+((a-3000)*.18)
    print("R$ %.2f"%tax)
elif a>=4500.01:
    tax=(1000*0.08)+(1500*.18)+((a-4500)*.28)
    print("R$ %.2f"%tax)