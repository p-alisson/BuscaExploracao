from tempera_simulada.classes import Ataque

mapeamento = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}

def imprimeTabuleiro(estado, indice=0):
    obj_atqs= Ataque(estado=estado)

    if obj_atqs.qtdAtaques:
        print("Ataques")
        obj_atqs.printAtaques()

    if indice == 0:
        imprimeTab(estado)

def imprimeTab(estado):
    tam_estado = len(estado)

    s = ""
    for i in (x for x in range(tam_estado)):
        s = s + " __{}__".format(mapeamento[i])
    print(s)

    for i in range(tam_estado):
        s = ""
        print("|     " * tam_estado + "|")
        for x in estado:
            if x == i:
                s = s + "|  {}  ".format("x")
            else:
                s = s + "|  {}  ".format(" ")
        print(s + "|" + str(i))
        print("|_____" * tam_estado + "|")