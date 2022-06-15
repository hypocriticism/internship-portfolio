import numpy as np
import random

class NN:
    def __init__(self, X, Y, LR):
        self.a = 1.0
        self.b = 2.0
        self.X = X
        self.Y = Y
        self.target = 0
        self.length = len(self.X)
        self.dim = len(self.X[0])
        self.W = np.zeros(self.dim)
        self.Batch_T = []
        self.Batch_NT = []
        self.C_P = 1.0
        self.C_N = 1.0
        self.C_a = 100.0
        self.LR = LR

    def init_Batch(self):
        for i in range(self.length):
            if i != self.target:
                if random.random() > 0.5:
                    self.Batch_T.append(i)
                else:
                    self.Batch_NT.append(i)
            else:
                self.Batch_T.append(i)

        
    def init_W(self, N):
        for i in range(self.dim):
            self.W[i] = N

    def ReLU(self, x):
        if x >= 0:
            return x
        else:
            return 0

    def dReLU(self, x):
        if x >= 0:
            return 1
        else:
            return 0
    
    def sReLU(self, x):
        if x < self.a:
            return 1
        elif x >= self.a and x < self.b:
            return (self.b - x) / (self.b - self.a)
        elif x >= self.b:
            return 0

    def dsReLU(self, x):
        if x < self.a:
            return 0
        elif x >= self.a and x < self.b:
            return 1 / (self.b - self.a)
        elif x >= self.b:
            return 0

    def FeedForward(self, p):
        WP = 0
        for i in range(self.dim):
            WP += (self.X[p][i] - self.X[self.target][i])**2 / self.W[i]**2
        z = WP**0.5 - self.a
        L = self.sReLU(z)
        return L, z

    def Train(self):
        for j in range(self.dim):
            J = 0
            T = 0
            N = 0
            dTdW = 0
            dNdW = 0
            for k in range(len(self.Batch_T)):
                L, z = self.FeedForward(self.Batch_T[k])
                if L != 0:
                    T += self.Y[self.Batch_T[k]] * L
                    N += L
                if L < 1 and L > 0:
                    dTdW -= self.Y[self.Batch_T[k]] * (1 / (self.b - self.a)) * (-(self.X[self.Batch_T[k]][j] - self.X[self.target][j])**2 / (z * self.W[j]**3))
                    dNdW -= (1 / (self.b - self.a)) * (-(self.X[self.Batch_T[k]][j] - self.X[self.target][j])**2 / (z * self.W[j]**3))

            self.W[j] += (self.C_P * (dTdW / N - dNdW * T / N**2) + self.C_N * self.dReLU(self.C_a - N) * dNdW) * self.LR
            J = self.C_P * T / N - self.C_N * self.ReLU(self.C_a - N)
            print(j, J)  

f = open("stockcodes.txt", "r")
s = f.read()
stockcodes = s.split()
f.close()

path = "C:/Users/user/Desktop/Python/어치/Core/Data Center/stockdata/"

for item in range(1):
    f = open(path+"Phasespace/Phasespace_"+stockcodes[item]+".txt", "r")
    s = f.readlines()
    dim = len(s[0].split()) - 2
    X = []
    Code = []
    Date = []

    for i in range(len(s)):
        X.append(s[i].split()[2:dim + 2])
        Code.append(s[i].split()[0])
        Date.append(s[i].split()[1])
        for j in range(len(X[i])):
            X[i][j] = float(X[i][j])
    f.close()

    f = open(path+"Label/Label_"+stockcodes[item]+".txt", "r")
    s = f.read()
    l = s.split()
    Y = np.zeros(len(l) // 3)
    for i in range(len(l)):
        if(i % 3 == 2):
            Y[i // 3] = float(l[i])
    f.close()
            
    NN1 = NN(X, Y, 0.1)
    
    Label_profit = []
    for i in range(len(Y)):
        if(Y[i] >= 2.0):
            Label_profit.append(i)
            
    NN1.target = Label_profit[0]
    NN1.init_Batch()
    NN1.init_W(1.0)
    
    for Epoch in range(10):
        NN1.Train()




                
                    
