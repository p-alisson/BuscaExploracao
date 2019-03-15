import numpy as np

class Cidade:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, cidade):
        x_dis = abs(self.x - cidade.x)
        y_dis = abs(self.y - cidade.y)
        distancia = np.sqrt((x_dis ** 2)+(y_dis ** 2))
        return distancia

    def __repr__(self):
        return "(" + str(self.x)+ "," + str(self.y) + ")"