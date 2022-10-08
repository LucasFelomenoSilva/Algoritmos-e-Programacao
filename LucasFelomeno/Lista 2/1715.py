#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715
cliente = int(input(""))
valorcompra = float(input(""))

if cliente == 1:
    print("Valor total a ser pago: R$%.2f" %valorcompra)
    
elif cliente == 2:
    compra = valorcompra * 0.13
    resultado2 = valorcompra - compra
    print("Valor total a ser pago: R$%.2f" %resultado2)

elif cliente == 3:
    compra = valorcompra * 0.07
    resultado3 = valorcompra - compra
    print("Valor total a ser pago: R$%.2f" %resultado3)

else:
    total = print("OPÇÃO INVÁLIDA!")
    compra = 0