from ts.classes import No
from random import randint, random, choice
from math import exp

sub_value = lambda l, i, v: l[:i] + [v] + l[i + 1:]
f = lambda S: calc_custo(S)

def calc_custo(estado):

    cont = 0
    tam = len(estado)
    a = [x + estado[x] for x in range(tam)]
    b = [x - estado[x] for x in range(tam)]
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if estado[i] == estado[j]:
                cont = cont + 1
            if a[i] == a[j]:
                cont = cont + 1
            if b[i] == b[j]:
                cont = cont + 1

    return cont

def temp_inicial():
    return randint(50, 100)


def pertuba(s):
    s = No(s)
    return rand_sucessor(s).estado

def randomiza():
    return random()

def rand_sucessor(atual):
    aux = [x for x in atual.estado]
    tam = len(aux)
    successor = []

    for i in range(tam):
        l = [x for x in range(tam) if not aux[i] == x]

        for j in l:
            k = sub_value(aux, i, j)
            successor.append(k)

    estado = choice(successor)
    custo = calc_custo(estado)
    no = No(estado=estado, valor=custo)
    return no

# SIMULATED ANNEALING
def simulated_annealing(s0, m=1000, p=100, l=10, alpha=0.99):
    s = s0
    t0 = temp_inicial()
    t = t0
    j = 1
    print(t)
    n_sucesso = 1
    while (n_sucesso != 0) and (j <= m):
        i = 1
        n_sucesso = 0
        print("Iteracao: " + str(j) + "| Temperatura: " + str(t))
        while (n_sucesso < l) and (i <= p):
            si = pertuba(s)
            delta_fi = f(si) - f(s)
            if delta_fi <= 0 or exp(-delta_fi / t) > randomiza():
                s = si
                print("Estado: {}".format(str(s)) + " | " + "Iteracao: {}".format(j) + " | " + "Ataques: {}".format(
                    calc_custo(s)))
                n_sucesso = n_sucesso + 1
            i = i + 1
        print("Numero de sucessos: " + str(n_sucesso))
        t = alpha * t
        j = j + 1

    return s