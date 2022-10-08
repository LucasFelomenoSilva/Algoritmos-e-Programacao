#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760
contador = 0
idade = 0
peso = 0
acumulador = 0
contador90 = 0
while contador < 4:
    idade = int(input(""))
    peso = float(input(""))
    contador = contador + 1
    acumulador = acumulador + idade
    if peso >= 90:
        contador90 = contador90 + 1
media = acumulador/4
print("Qtd pessoas > 90Kg: %i"%contador90)
print("Idade média: %.2f"%media)