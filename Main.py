import Telefone,CPF,Email,time

entS = [] # entrada separada

while True:
    RM = int(input("""Qual dos identificadores de validade voce quer usar
    [0] Numero de Telefone
    [1] CPF
    [2] Email
    """))
    ent = input("Qual o termo que voce quer validar? ")
    if RM == 0:
        Telefone.Telefone(ent)
    elif RM == 1:
        CPF.CPF(ent)
    elif RM == 2:
        Email.Email(ent)
    else:
        print("Tu é burro pra krl")
    time.sleep(10)

