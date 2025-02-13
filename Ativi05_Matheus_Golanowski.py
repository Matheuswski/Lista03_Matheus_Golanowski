#Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. Se ele responder "sim", pergunte se está ventando. Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário, exiba a mensagem "Pegue um guarda-chuva". Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".
chuva = (input("esta chovendo?").lower)

if chuva == "SIM".lower():
    vento = input("Esta ventando?").lower()
    
    if vento == "SIM":
        print("Esta vetando muito para um guarda-chuva")
        print("Matheus Golanowski")
    if vento == "NÃO":
        print("Pegue um guarda-chuva")
        print("Matheus Golanowski")
    else:
        print("Aproveite o seu dia")
        print("Matheus Golanowski")