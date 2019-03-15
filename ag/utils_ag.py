import random, operator

from ag.fitness import Fitness


def gera_rotas(list_cidade):
    rota = random(list_cidade, len(list_cidade))
    return rota

def populacao_inicial(tam_pop, list_cidade):
    populacao = []
    for i in range(0, tam_pop):
        populacao.append(gera_rotas(list_cidade))
    return populacao

def rank_rotas(populacao):
    result_fitness = {}
    for i in range(0, len(populacao)):
        result_fitness[i] = Fitness(populacao[i]).rota_fitness()
    return sorted(result_fitness.items(), key = operator.itemgetter(1), reverse = True)