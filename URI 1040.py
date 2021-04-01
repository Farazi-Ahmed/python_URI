# 1040

value=input().split(" ")
n1,n2,n3,n4 = value

avg = ((2*float(n1)) + (3*float(n2)) + (4*float(n3)) + (1*float(n4))) / (2+3+4+1)

print("Media: %.1f"%avg)

if avg>=7:
    print("Aluno aprovado.")
elif avg<5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exam=float(input())
    print("Nota do exame: %.1f"%exam)
    avg2 = (exam+avg)/2
    
    if avg2>=5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f"%avg2)