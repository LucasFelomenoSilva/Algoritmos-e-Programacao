#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733
nome = input("")
horastrabalhadas = float(input(""))

salariominimo = 1192.40
valorhe = 10

salarioextra = horastrabalhadas * valorhe
salariobruto = 3 * salariominimo + salarioextra
salarioinicial = 0

if salariobruto > 2000:
  inss = salariobruto * 0.12
else: 
  inss = salariobruto * 0.5
if salariobruto > 2500:
  ir = salariobruto * 0.20
else: 
  ir = salariobruto * 0.0
 
salarioliquido = salariobruto - inss - ir

print("Nome: %s" %(nome));
print("Salário bruto: R$%.2f" %(salariobruto))
print("Salário líquido: R$%.2f" %(salarioliquido))