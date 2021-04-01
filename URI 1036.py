# 1036
value = input().split(" ")
a,b,c = value

if float(a)!=0:
    if (float(b)**2 - (4*float(a)*float(c)))>=0:
        R1 = (-float(b)+(float(b)**2 - (4*float(a)*float(c)))**0.5)/(2*float(a))
        R2 = (-float(b)-(float(b)**2 - (4*float(a)*float(c)))**0.5)/(2*float(a))
        print("R1 = %.5f"%R1)
        print("R2 = %.5f"%R2)
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")