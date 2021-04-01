#1115
x,y = map(int, input().split())

while (x!=0) or (y!=0):
    if x>0:
        if y>0:
            print("primeiro")
        elif y<0:
            print("quarto")
    elif x<0:
        if y>0:
            print("segundo")
        elif y<0:
            print("terceiro")
    x,y = map(int, input().split())