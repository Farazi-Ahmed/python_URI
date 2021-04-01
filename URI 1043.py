# 1043

value = map(float,input().split(" "))
a,b,c = value

if (a+b)>c and (a+c)>b and (b+c)>a:
    sum = a+b+c
    print("Perimetro = %.1f"%sum)
else:
    area = (0.5 * (a+b))*c
    print("Area = %.1f"%area)