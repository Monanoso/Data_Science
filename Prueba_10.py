import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import random

#******Expresión para realizar una lista con bucles FOR en una sola linea*****
#matriz = [[random.uniform(0,1) for i in range(n)] for j in range(n)]


def estimar_pi(n):
    num_puntos_circle = 0
    num_puntos_total = 0
    matriz = np.random.uniform(-1,1, size=(n,2))

    for i in range(n):
        distancia = matriz[i,0]**2 + matriz[i,1]**2
        if distancia <= 1:
            num_puntos_circle += 1
            plt.scatter(x=matriz[i,0],y=matriz[i,1],marker='o', c='r')
        else:
            plt.scatter(x=matriz[i,0],y=matriz[i,1],marker='o', c='b')
        num_puntos_total += 1

        if num_puntos_total % 500 == 0 :
            print(num_puntos_total)

    

    pi_calculado = 4 * (num_puntos_circle/num_puntos_total)

    #print(matriz)
    print(pi_calculado)
    plt.show()


estimar_pi(9000)


"""for i in range(n):
    print(matriz[i][0])
    print(matriz[i][1])"""
