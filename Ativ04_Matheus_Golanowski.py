#Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho", caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
cor = input("Digite sua cor favorita :")

if cor == "vermelho":
    print("Eu tambem gosto de vermelho")
    print("Matheus Golanowski")
elif cor == "VERMELHO":
    print("Eu tambem gosto de vermelho")
    print("Matheus Golanowski")
elif cor == "Vermelho":
    print("Eu tambem gosto de vermelho")
    print("Matheus Golanowski")

else:
    print("Eu não gosto de {}, eu prifiro vermelho".format(cor))
    print("Matheus Golanowski")