#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713
sal_hora = float(input(""))
mes = float(input())
sal_bruto = sal_hora*mes
leao = sal_bruto*0.11
inss = sal_bruto*0.08
sindicado = sal_bruto*0.05
sal_liquido = sal_bruto - leao - inss - sindicado
print("Salário bruto: R$%.2f"%sal_bruto)
print("Imposto: R$%.2f"%leao)
print("INSS: R$%.2f"%inss)
print("Sindicato: R$%.2f"%sindicado)
print("Líquido: R$%.2f"%sal_liquido)