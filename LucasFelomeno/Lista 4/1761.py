#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761
preco = 1
total = 0

while preco > 0:
    preco = float(input(""))
    total += preco 

    
dinheiro = float(input(""))    

print("Total da compra: R$%.2f" %(total))
print("Valor pago: R$%.2f" %(dinheiro))
print("Troco: R$%.2f" %(dinheiro - total))