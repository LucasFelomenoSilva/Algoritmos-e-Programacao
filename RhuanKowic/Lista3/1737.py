#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737
quantidade_num = int(input())
acumulador = 0
n = 0
if quantidade_num <= 0:
    print("Informe uma quantidade > 0!")
else:
    while quantidade_num > 0:
        quantidade_num = quantidade_num - 1
        n = int(input())
        acumulador = acumulador + n
    print("Soma dos números informados: %.2f"%acumulador)
