def Telefone(ent):
    ATR = "1234567890" #alfabeto numero de telefone/RG
    filt="()-" #simbolos ignorados
    Validade = True
    entS=[]
    for i in ent: #Separa a entrada em uma lista
        if i not in filt:
            entS.append(i)
    for i in range(0,len(entS)):
        if entS[i] not in ATR: # se algum termo não estiver no alfabelo, ele não aceita
            Validade = False
            break
        if i > 10: # se o tamanho for maior que 11 termos, ele nao aceita
            Validade = False
            break
        count = i
    if count < 10: # se o tamanho for menor que 11 termos, ele nao aceita
        Validade = False

    if Validade == True:
        print("Entrada aceita")
    else:
        print("Entrada não Aceita")
    