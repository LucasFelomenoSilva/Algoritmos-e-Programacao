#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734
num = int(input(""))
n = num
x = 1
while num > 0:
    x *= num
    num -= 1

print("%i! = %i"%(n, x))