import networkx as nx
import numpy as np
np.set_printoptions(threshold=np.nan)

#Começo da matriz de transição
Q = [[0 for x in range(36)] for y in range(36)]
for i in range(0,36):
    for j in range (0,36):
        # escadas
        if i in [2-1, 5-1, 9-1, 18-1, 25-1]:
            if i == 2-1:
                if j == 15-1:
                    Q[i][j] = 1.0
            elif i == 5-1:
                if j == 7-1:
                    Q[i][j] = 1.0
            elif i == 9-1:
                if j == 27-1:
                    Q[i][j] = 1.0
            elif i == 18-1:
                if j == 29-1:
                    Q[i][j] = 1.0
            elif i == 25-1:
                if j == 35-1:
                    Q[i][j] = 1.0
        #cobras
        elif i in [17-1, 20-1, 24-1, 32-1, 34-1]:
            if i == 17-1:
                if j == 4-1:
                    Q[i][j] = 1.0
            if i == 20-1:
                if j == 6:
                    Q[i][j] = 1.0
            if i == 24-1:
                if j == 16:
                    Q[i][j] = 1.0
            if i == 32-1:
                if j == 30:
                    Q[i][j] = 1.0
            if i == 34-1:
                if j == 12:
                    Q[i][j] = 1.0
        else:
            # print(j)
            if j == i + 1 or j == i + 2:
                Q[i][j] = 1/2
            else:
                Q[i][j] = 0
for i in range(36):
    print (Q[i])
#Fim matriz de transição

#Início do Power Method com k=100
print("O jogador inicia na casa 1, ou seja: \n w(0) = [1, 0, 0, 0, ... 0]")
w = []
for i in range(0,36):
    if (i == 0):
        w.append(1)
    else:
        w.append(0)

#início do power method
for i in range (100):
    w = np.dot(w,Q)
print ("Depois de 100 jogadas, a probabilidade de estar em cada casa é: ")
for i in range(len(w)):
    print ("Casa " + str(i + 1) + ": " + str(w[i]))





