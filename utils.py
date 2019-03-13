from classes import Ataque

alphabet = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J",
            10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T",
            20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}

# def imprimeTabuleiro(estado, indice=0):
#     obj_atqs= Ataque(estado=estado)
#
#     if obj_atqs.qtdAtaques:
#         print("Ataques")
#         obj_atqs.printAtaques()
#
#     if indice == 0:
#         imprimeTab(estado)

def imprimeTabuleiro(estado):
    tam_estado = len(estado)

    s = ""
    for i in (x for x in range(tam_estado)):
        s = s + " __{}__".format(alphabet[i])
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