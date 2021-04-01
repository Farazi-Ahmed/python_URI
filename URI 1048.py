# 1048

salary = float(input())

if (salary>=0 and salary <= 400.00):
    rate = 0.15
elif (salary>=400.01 and salary<=800.00):
    rate = 0.12
elif (salary>=800.01 and salary<=1200.00):
    rate = 0.10
elif (salary>=1200.01 and salary<=2000.00):
    rate = 0.07
else:
    rate = 0.04

print("Novo salario: %.2f"%(salary + (rate * salary)))
print("Reajuste ganho: %.2f"%(rate * salary))
#print("Em percentual: %d %d"%(rate * 100, "%"))

print("Em percentual: {} {}".format(rate * 100,"%"))