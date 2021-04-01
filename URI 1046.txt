# 1046

a,b = map(int, input().split())

if b>a:
    time = b-a
elif a>b:
    time = (b+24) - a
else:
    time = 24
print("O JOGO DUROU %i HORA(S)"%time)