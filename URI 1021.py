#1021
N= float(input())

hundred=fifty=twenty=ten=five=two=0
one=fiftycents=twentyfivecents=tencents=fivecents=onecent=0
num=0
num=N

while N!=0:
    if N>=100:
        hundred=N//100
        N=N%100
    elif N>=50:
        fifty=N//50
        N=N%50
    elif N>=20:
        twenty=N//20
        N=N%20
    elif N>=10:
        ten=N//10
        N=N%10
    elif N>=5:
        five=N//5
        N=N%5
    elif N>=2:
        two=N//2
        N=N%2
    elif N>=1:
        one=N//1
        N=N%1
    elif N>=0.5:
        fiftycents=N//0.5
        N=N%0.5
    elif N>=0.25:
        twentyfivecents=N//0.25
        N=N%0.25
    elif N>=0.1:
        tencents=N//0.1
        N=N%0.1
    elif N>=0.05:
        fivecents=N//0.05
        N=N%0.05
    else:
        onecent=round(N,2)*100
        N=0
        
print("NOTAS:")
print("%i nota(s) de R$ 100.00"%hundred)
print("%i nota(s) de R$ 50.00"%fifty)
print("%i nota(s) de R$ 20.00"%twenty)
print("%i nota(s) de R$ 10.00"%ten)
print("%i nota(s) de R$ 5.00"%five)
print("%i nota(s) de R$ 2.00"%two)
print("MOEDAS:")
print("%i nota(s) de R$ 1.00"%one)
print("%i nota(s) de R$ 0.50"%fiftycents)
print("%i nota(s) de R$ 0.25"%twentyfivecents)
print("%i nota(s) de R$ 0.10"%tencents)
print("%i nota(s) de R$ 0.05"%fivecents)
print("%i nota(s) de R$ 0.01"%onecent)