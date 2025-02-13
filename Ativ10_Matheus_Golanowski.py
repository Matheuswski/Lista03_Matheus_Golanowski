#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
salario = float(input("Qual seu salario: "))

if salario > 1250.00:
    nsalario = salario + (salario * 0.10)
    print("seu salario de R$", salario * 0.10, "Sofreu um aumento de R$",nsalario)
    print("Matheus Golanowski")
elif salario <= 1250.00:
    nsalario = salario + (salario - 0.15)
    print("seu salario de R$", salario * 0.15, "Sofreu um aumento de R$",nsalario)
    print("Matheus Golanowski")