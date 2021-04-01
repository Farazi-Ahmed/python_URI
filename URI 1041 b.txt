# 1041 (another way)

value = input().split(" ")
x,y = value

if float(x)==0 and float(y)==0:
    print("Origem")
elif float(x)==0 and float(y)!=0:
    print("Eixo Y")
elif float(y)==0 and float(x)!=0:
    print("Eixo X")
elif float(x)>0 and float(y)>0:
    print("Q1")
elif float(x)>0 and float(y)<0:
    print("Q4")
elif float(x)<0 and float(y)>0:
    print("Q2")
else:
    print("Q3")