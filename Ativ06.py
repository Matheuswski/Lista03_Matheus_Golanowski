#Pergunte a idade do usuário. Se tiver 16 anos ou mais, exiba a mensagem "Você pode votar", se tiver 18 anos, exiba a mensagem "Você pode aprender a dirigir", se tiver 14 anos, exiba a mensagem "Você pode comprar um bilhete de loteria", se tiver menos de 14 anos, exiba a mensagem "Você pode fazer doces ou travessuras".
idade = input("Digite sua idade :")

if idade == 16:
    print("Você pode votar")
    print("Matheus")
    
elif idade >= 18:
    print("Você pode aprender a dirigir")
    print("Matheus")
elif idade == 14:
    print("Você pode comprar um bilhete de loterica")
    print("Matheus")
elif idade < 14:
    print("Você pode fazer doces ou travesuras.")
    print("Matheus")