def Email(ent):
    AE = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.+-" # ALFABETO EMAIL
    print("A expressão regular do validador de email é A=([a-zA-Z0-9_+-]\n([a-zA-Z0-9_+-]@[a-zA-Z0-9_.+-].[a-zA-Z0-9_+-])")
    entS=[[],[],[]]
    Validade = True
    for j in range(0,2):
        for i in ent:
            if j == 0:
                if i == "@":
                    j+=1
                else:
                    entS[j].append(i)
            if j == 1:
                if i == ".":
                    j+=1
                else:
                    entS[j].append(i)
            else:
                entS[j].append(i)
    for i in range(0,len(entS)):
        for j in range(0,len(ent[i])):
            if entS[j][i] not in AE: # se algum termo não estiver no alfabelo, ele não aceita
                Validade = False
            break
    if Validade == True:
        print("Entrada aceita")
    else:
        print("Entrada não Aceita")