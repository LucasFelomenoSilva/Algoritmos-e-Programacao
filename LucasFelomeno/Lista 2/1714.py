#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714
compra = float(input(""))

if compra < 20:
    valor = compra * 1.45

else:
    valor = compra * 1.30

print("Valor de venda:R$%.2f" %valor)