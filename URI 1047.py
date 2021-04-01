# 1047

a,b,c,d = map(int,input().split())

start = (a * 60) + b
end = (c * 60) + d
time = 0

if c<a:
    time = end - start + (24*60)
    hour = time//60
    print(time)
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hour,time%60))
elif c==a:
    time = end - start
    if d<b:
      hour = 23
      print(time)
      print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hour,time%60))
    else:
      hour = 24
      mins = 0
      print(time)
      print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hour,mins))
else:
    time = end - start
    hour = time//60
    print(time)
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hour,time%60))