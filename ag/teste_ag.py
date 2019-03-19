from ag.cidade import Cidade
from ag.algoritmo_genetico import *
import random

def main():
    lista_cidades = []
    for i in range(0, 25):
        lista_cidades.append(Cidade(x=int(random.random() * 200), y=int(random.random() * 200)))

    algoritmo_genetico_plot(populacao=lista_cidades, tam_pop=100, tam_elite=20, taxa_mutacao=0.01, geracoes=500)

if __name__ == "__main__":
    main()