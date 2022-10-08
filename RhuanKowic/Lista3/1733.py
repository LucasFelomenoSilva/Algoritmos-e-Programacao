#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733
sal_min = 1192.40
valor_hrextra = 10
inss = 0
leao = 0
nome = str(input(""))
hr_extra = float(input(""))

salario_hora_extra = hr_extra * valor_hrextra
salario_bruto = 3 * sal_min + salario_hora_extra
if salario_bruto > 2000:
    inss = salario_bruto * 0.12
else:
    inss =salario_bruto * 0.05

if salario_bruto > 2500:
    leao = salario_bruto * 0.20
else:
    leao = salario_bruto + 0
salario_liquido = salario_bruto - inss - leao
print("Nome: %s"%(nome));
print("Salário bruto: R$%.2f"%salario_bruto)
print("Salário líquido: R$%.2f"%salario_liquido)