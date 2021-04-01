# 1041

value = input().split(" ")
x,y = value

if float(x)==0:
    if float(y)==0:
        print("Origem")
    else:
        print("Eixo Y")
elif float(y)==0:
    if float(x)!=0:
        print("Eixo X")
elif float(x)>0:
    if float(y)>0:
        print("Q1")
    else:
        print("Q4")
elif float(x)<0:
    if float(y)>0:
        print("Q2")
    else:
        print("Q3")