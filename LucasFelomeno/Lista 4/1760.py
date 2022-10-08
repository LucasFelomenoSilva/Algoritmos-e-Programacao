#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760
quantidadedePessoas = 0
acimapeso = 0
mediaidade = 0

while quantidadedePessoas < 4:
    idade = int(input(""))
    peso = float(input(""))
    quantidadedePessoas = quantidadedePessoas + 1
    if peso > 90:
        acimapeso = acimapeso + 1

    mediaidade = mediaidade + idade

print("Qtd pessoas > 90 Kg: %i"%(acimapeso))
print("Idade média: %.2f"%(mediaidade / 4))