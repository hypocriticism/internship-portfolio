import matplotlib.pyplot as plt
import math
import numpy as np
import random

def sigmoid(x, alpha):
    e = 2.71828
    big = e**30 - 1
    if(alpha * x < 30):
        return 1.0 / (1.0 + e**(alpha * x))
    else:
        return 1.0 / (1.0 + big)

def Makebatch(Range, Num, Target):
    Batch = []
    for i in range(Num):
        Batch.append(random.randint(Range[0], Range[1]))
    Batch.append(Target)
    return Batch


class NN:
    def __init__(self, Dim, Alpha, P_Target):
        self.dim = Dim
        self.W = np.zeros(self.dim)
        self.target = P_Target
        self.alpha = Alpha
        self.R = 1.0

    def initW(self, N):
        for i in range(self.dim):
            self.W[i] = N
    
    def FeedForward(self, P):
        WP = 0
        for i in range(self.dim):
            WP += (self.W[i]*self.target[i] - self.W[i]*P[i])**2
        z = WP - self.R
        L = sigmoid(z, self.alpha)
        return L


    def train(self, batch, P, Y, LR):
        _W = np.zeros(self.dim)
        for i in range(len(batch)):
            L = self.FeedForward(P[batch[i]])
            for j in range(self.dim):
                _W[j] += -Y[batch[i]] * self.alpha * L * (1 - L) * 2 * (self.W[j] * P[batch[i]][j] - self.W[j] * self.target[j]) * (P[batch[i]][j] - self.target[j])
        
        for j in range(self.dim):
            self.W[j] += _W[j] * LR

    def profit(self, batch, P, Y):
        profit = 0
        Num = 0
        profitlist = []
        for i in range(len(batch)):
            L = self.FeedForward(P[batch[i]])
            if(L >= 0.5):
                profit += Y[batch[i]]
                Num += 1
                profitlist.append(batch[i])
        if(len(profitlist) < 10):
            return [profit, Num, profitlist]
        else:
            return [profit, Num]

dim = 30
N = 500
D = []

f = open("Phasespace.txt", "r")
s = f.readlines()
for i in range(len(s)):
    D.append(s[i].split())
    for j in range(len(D[i])):
        D[i][j] = float(D[i][j])
f.close()

f = open("Label.txt", "r")
s = f.read()
L = s.split()
for i in range(len(L)):
    L[i] = float(L[i])
f.close()
    

L_profit = []

for i in range(len(L)):
    if(L[i] > 3):
        L_profit.append(i)

f = open("Weight.txt", "w")
f.close()
for i in range(len(L_profit)):
    TEST = L_profit[i]

    NN1 = NN(dim, 1.0, D[TEST])
    NN1.initW(0.01)


    B = np.arange(len(D), dtype = int)

    for Epoch in range(1000):
        Batch = Makebatch([0, len(D) - 1], 200, TEST)
        NN1.train(Batch, D, L, 0.0001)
    
    Nprofit = NN1.profit(B, D, L)
    if(Nprofit[1] != 0):
        if(Nprofit[0] / Nprofit[1] > 1 and Nprofit[1] > 30):
            f = open("Weight.txt", "a")
            for j in range(len(NN1.W)):
                f.write("%.6f "%NN1.W[j])
            f.write("\n")
            for j in range(len(D[TEST])):
                f.write("%.6f "%D[TEST][j])
            f.write("\n")
            print(Nprofit)
            print(TEST)
            f.write("%.3f "%Nprofit[0])
            f.write("%d "%Nprofit[1])
            f.write("%d"%TEST)
            f.write("\n\n")
            f.close()
