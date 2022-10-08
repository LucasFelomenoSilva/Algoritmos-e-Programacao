#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714
produto = float(input(""))
if produto < 20.00:
    valor_final = produto*1.45
    print("Valor de venda: R$%.2f"%valor_final)
else:
    valor_final = produto*1.30
    print("Valor de venda: R$%.2f"%valor_final)