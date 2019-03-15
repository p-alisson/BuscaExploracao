from tempera_simulada.tempera_simulada import simulated_annealing
from tempera_simulada.utils import imprimeTabuleiro

def main():
    estado_inicial = [2, 0, 6, 4, 7, 1, 3, 5]

    print("o estado atual é: ")
    imprimeTabuleiro(estado_inicial)

    estado = simulated_annealing(estado_inicial, 1000, 100, 10)
    imprimeTabuleiro(estado)

if __name__ == "__main__":
    main()