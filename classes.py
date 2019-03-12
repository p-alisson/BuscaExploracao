class Problema(object):

    def __init__(self, inicio, objetivo=None, acao=None):
        self.inicio = inicio
        self.objetivo = objetivo
        self.acao = acao

    def test_objetivo(self, estadoNo):
        return estadoNo == self.objetivo

    def acoes(self,estadoNo):
        return list(self.acao[estadoNo])

class No(object):
    def __init__(self, estado, pais=None, acao=None, custo_caminho=0, valor=None):
        self.estado = estado
        self.pais = pais
        if pais:
            self.acao = pais.estado + "->" + estado
        self.custo_caminho = custo_caminho
        self.valor = valor
        self.profundidade = 0
        if pais:
            self.profundidade = pais.profundidade + 1

    def __repr__(self):
        return self.estado + ", " + self.acao

class Ataque(object):

    def __init__(self, ataques=[], estado=[]):
        self.ataques = ataques
        self.qtdAtaques = 0

    def addAtaques(self, i, j):
        self.ataques.append((i,j))


    def printAtaques(self):
        d = {}
        for i in self.ataques:
            if i[0] in d:
                d[i[0]].append(i)
            else:
                d[i[0]] = [i]

        for i in d:
            s = "{}: (".format(1)
            for x in d[i]:
                if not x == d[i][-1]:
                    s = s + x[0] + " <-> " + x[1] + ") ("
                else:
                    s = s + x[0] + " <-> " + x[1] +")"
            print(s)

    def contAtaques(self, estado):
        atqs = []
        cont = 0
        tam = len(estado)
        a = [x+estado[x] for x in range(tam)]
        b = [x+estado[x] for x in range(tam)]
        for i in range(tam -1):
            for j in range(i+1, tam):
                if estado[i] == estado[j]:
                    k, l = str(estado[i]) + str(i), str(estado[j]) + str(j)
                    atqs.append((k, l))
                    cont = cont +1
                if a[i] == a[j]:
                    k, l = str(a[i]-i) + str(i), str(a[j]-j) + str(j)
                    atqs.append((k, l))
                    cont = cont +1
                if b[i] == b[j]:
                    k, l = str(i-b[i]) + str(i), str(j-b[j]) + str(j)
                    atqs.append((k, l))
                    cont = cont +1
        return atqs, cont