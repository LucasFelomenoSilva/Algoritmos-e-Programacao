#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715
num = int(input(""))
valor = float(input(""))
if num == 1:
    valor_final = valor
    print("Valor total a ser pago: R$%.2f"%valor_final)
elif num == 2:
    valor_final = valor*0.87
    print("Valor total a ser pago: R$%.2f"%valor_final)
elif num == 3:
    valor_final = valor*0.93
    print("Valor total a ser pago: R$%.2f"%valor_final)
else:
    print("OPÇÃO INVÁLIDA!")