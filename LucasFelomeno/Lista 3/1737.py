#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737
n = int(input(""))
i = 1 
acc = 0 

if i < n:
    while i <= n:
        a = float(input(""))
        acc = acc + a
        i = i + 1 
    print("Soma dos números informados: %.2f" %(acc))
else:
    print("Informe uma quantidade > 0!")