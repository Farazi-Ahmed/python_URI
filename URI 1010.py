# 1010

value1 = input (). split ()

prod1code, prod1units, prod1price = value1

value2 = input (). split ()

prod2code, prod2units, prod2price = value2

value = (int(prod1units)*float(prod1price)) + (int(prod2units)*float(prod2price))

print("VALOR A PAGAR: R$ %.2f"%value)