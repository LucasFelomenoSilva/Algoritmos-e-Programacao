#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761
produto = float(input(""))
troco = 0
acumulador = 0
while produto > 0:
    acumulador = acumulador + produto
    produto = float(input(""))

val_pago = float(input(""))
troco = val_pago - acumulador

print("Total da compra: R$%.2f"%acumulador)
print("Valor pago: R$%.2f"%val_pago)
print("Troco: R$%.2f"%troco)