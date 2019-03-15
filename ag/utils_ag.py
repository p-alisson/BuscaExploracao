import random, operator, numpy as np, pandas as pd

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
    return sorted(result_fitness.items(), key=operator.itemgetter(1), reverse=True)

def selecao(pop_ranked, tam_elite):
    result_selecao = []
    df = pd.DataFrame(np.array(pop_ranked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range(0, tam_elite):
        result_selecao.append(pop_ranked[i][0])
    for i in range(0, len(pop_ranked) - tam_elite):
        pick = 100 * random.random()
        for i in range(0, len(pop_ranked)):
            if pick <= df.iat[i, 3]:
                result_selecao.append(pop_ranked[i][0])
                break
    return result_selecao