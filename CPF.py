def CPF(ent):
    ATR = "1234567890"
    Validade = True
    entS = []
    for i in ent:
        entS.append(i)
    try:
        for i in range(0,4):
            if i < 2:
                for j in range(0,4):
                    if j != 3:
                        if entS[j+(i*4)] not in ATR:
                            Validade = False
                    else:
                        if entS[j+(i*4)] != ".":
                            Validade = False
            elif i == 2:
                for j in range(0,4):
                    if j != 3:
                        if entS[j+(i*4)] not in ATR:
                            Validade = False
                    else:
                        if entS[j+(i*4)] != "-":
                            Validade = False
            else:
                for j in range(12, len(entS)):
                    if j >= 14:
                        Validade = False
                    else:
                        if entS[j] not in ATR:
                            Validade = False
                            break
    except (RuntimeError, TypeError, NameError):
        Validade = False
    if Validade == True:
        print("Entrada aceita")
    else:
        print("Entrada não Aceita")
