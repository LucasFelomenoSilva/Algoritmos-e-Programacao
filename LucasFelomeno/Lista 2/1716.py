#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716
func = (input(""))
salario = float(input(""))

if func == 'A':
    total1 = salario * 0.10
    resultado1 = total1 + salario
    print("Novo salário: R$%.2f" %resultado1)
    
elif func == 'B':
    total2 = salario * 0.15
    resultado2 = total2 + salario
    print("Novo salário: R$%.2f" %resultado2)


elif func == 'C':
    total3 = salario * 0.20
    resultado3 = total3 + salario
    print("Novo salário: R$%.2f" %resultado3)