#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716
letra = input("")
salario_atual = float(input(""))
if letra == "A":
    salario_final = salario_atual*1.10
    print("Novo salário: R$%.2f"%salario_final)
elif letra == "B":
    salario_final = salario_atual*1.15
    print("Novo salário: R$%.2f"%salario_final)
elif letra == "C":
    salario_final = salario_atual*1.20
    print("Novo salário: R$%.2f"%salario_final)
else:
    print("")