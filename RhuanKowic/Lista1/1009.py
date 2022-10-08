#https://www.beecrowd.com.br/judge/pt/problems/view/1009
nome_vendedor = str(input(""))
salario_fixo = float(input(""))
valor_venda = float(input(""))
comissao = valor_venda*0.15
salario_comissao = salario_fixo+comissao
print("TOTAL = R$ %.2f"%salario_comissao)