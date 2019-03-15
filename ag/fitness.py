class Fitness:
    def __init__(self, rota):
        self.rota = rota
        self.distancia = 0
        self.fitness = 0.0

    def distancia_rota(self):
        if self.distancia == 0:
            dis_caminho = 0
            for i in range(0, len(self.rota)):
                desde_cidade = self.rota[i]
                ate_cidade = None
                if i+1 < len(self.rota):
                    ate_cidade = self.rota[i + 1]
                else:
                    ate_cidade = self.rota[0]
                dis_caminho += desde_cidade.distancia(ate_cidade)
            self.distancia = dis_caminho
        return self.distancia

    def rota_fitness(self):
        if self.fitness == 0:
            self.fitness = 1/float(self.distancia_rota())
        return self.fitness