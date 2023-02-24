def CPF(ent):
    ATR = "1234567890" #alfabeto numero de telefone/RG
    Validade = True
    entS=[[],[],[],[]]
    count = 0
    for j in range(0,4):
        for i in ent: #Separa a entrada em uma lista
            if i == "." or i == "-":
                j=+1
            else:
                entS[j].append(i)
    for j in range(0,4):
        for i in range(0,len(entS[j])):
            if entS[j][i] not in ATR: # se algum termo não estiver no alfabelo, ele não aceita
                Validade = False
                break
            if count > 10: # se o tamanho for maior que 11 termos, ele nao aceita
                Validade = False
                break
            count+=1
    if count < 10: # se o tamanho for menor que 11 termos, ele nao aceita
        Validade = False

    if Validade == True:
        print("Entrada aceita")
    else:
        print("Entrada não Aceita")