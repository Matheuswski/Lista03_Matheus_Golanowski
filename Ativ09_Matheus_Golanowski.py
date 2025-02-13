#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal
renda = int(input("qual sua renda: "))

if renda <= 2259.20:
    print("Voce não paga impostos")
elif renda >= 2259.21 and renda <= 2826.65:
    imposto = renda * 0.075
    print("imposto de renda de {} ".format(imposto))

elif renda >= 2826.66 and renda <= 3751.05:
    imposto = renda * 0.150
    print("imposto de renda  de {} ".format(imposto)) 

elif renda >= 3751.06 and renda <= 4664.68:
    imposto = renda * 0.220
    print("imposto de renda  de {} ".format(imposto))

else:
    imposto = renda * 0.275
    print("imposto de renda  de {} ".format(imposto))