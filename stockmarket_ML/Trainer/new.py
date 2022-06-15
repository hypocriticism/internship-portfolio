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


    def train(self, batch, D, Y, LR):
        _W = np.zeros(self.dim)
        for i in range(len(batch)):
            L = self.FeedForward(D[batch[i]])
            for j in range(self.dim):
                #_W[j] += -Y[batch[i]] * self.alpha * L * (1 - L) * 2 * (self.W[j] * P[batch[i]][j] - self.W[j] * self.target[j]) * (P[batch[i]][j] - self.target[j])
                if(Y[batch[i]] < 0):
                    _W[j] += -1.01 * Y[batch[i]] * self.alpha * L * (1 - L) * 2 * (self.W[j] * D[batch[i]][j] - self.W[j] * self.target[j]) * (D[batch[i]][j] - self.target[j])
                else:
                    _W[j] += -1.0 * Y[batch[i]] * self.alpha * L * (1 - L) * 2 * (self.W[j] * D[batch[i]][j] - self.W[j] * self.target[j]) * (D[batch[i]][j] - self.target[j])
        
        for j in range(self.dim):
            self.W[j] += _W[j] * LR

    def profit(self, batch, P, Y, Date, Code, Filename):
        profit = 0
        Num = 0
        profitlist = []
        f1 = open(Filename, "a")
        cost = 0
        for i in range(len(batch)):
            L = self.FeedForward(P[batch[i]])
            cost += L * Y[batch[i]]
            if(L >= 0.1):
                profit += Y[batch[i]]
                f1.write(Date[batch[i]]+" "+Code[batch[i]]+" "+"%.2f\n"%Y[batch[i]])
                Num += 1
                profitlist.append(batch[i])
        f1.close()
        if(len(profitlist) < 10):
            return [cost, profit, Num, profitlist]
        else:
            return [cost, profit, Num]

f = open("stockcodes.txt", "r")
s = f.read()
stockcodes = s.split()
f.close()

D = []
Date = []
Code = []
path = "C:/Users/user/Desktop/Python/어치/Core/Data Center/stockdata"



for item in range(1):
    f = open(f"{path}/Phasespace/Phasespace_{stockcodes[item]}.txt", "r")
    s = f.readlines()
    dim = len(s[0].split()) - 2
    for i in range(len(s)):
        D.append(s[i].split()[2:dim + 2])
        Code.append(s[i].split()[0])
        Date.append(s[i].split()[1])
        for j in range(len(D[i])):
            D[i][j] = float(D[i][j])
    f.close()
    
    Batch_NT = np.arange(len(D) // 2, len(D), dtype = int)
    Batch_T = np.arange(len(D) // 2, dtype = int)

    f = open(f"{path}/Label/Label_{stockcodes[item]}.txt", "r")
    s = f.read()
    Label = s.split()
    Label = [float(l.split()[2]) for l in Label]
    f.close()
    
    Label_profit = [l for l in Label if l>2.0]

    f = open(f"Hypersphere/Hypersphere_{stockcodes[item]}.txt", "w")
    f.close()
    
    for i in range(len(Label_profit) // 2):
        TEST = Label_profit[i]

        NN1 = NN(dim, 2.0, D[TEST])
        NN1.initW(0.25)

        for Epoch in range(10):
            #Batch = Makebatch([0, len(D) // 2 - 1], 200, TEST)
            Bcost = NN1.profit(Batch_T, D, Label, Date, Code, "temp.txt")
            Ncost = NN1.profit(Batch_NT, D, Label, Date, Code, "temp.txt")
            
            print(f"Bcost: {Bcost[0]:.2f} {Bcost[1]:.2f} {Bcost[2]:.2f} {(Bcost[1] / Bcost[2]):.2f}")
            print(f"Ncost: {Ncost[0]:.2f} {Ncost[1]:.2f} {Ncost[2]:.2f} {(Ncost[1] / Ncost[2]):.2f}")
            print("")
            
            NN1.train(Batch_T, D, Label, 0.01)
            
        f = open("result_"+stockcodes[item]+"/result_"+"%d_"%i+stockcodes[item]+"_N.txt", "w")
        f.write("")
        f.close()
        f = open("result_"+stockcodes[item]+"/result_"+"%d_"%i+stockcodes[item]+"_B.txt", "w")
        f.write("")
        f.close()
        Nprofit = NN1.profit(Batch_NT, D, Label, Date, Code, "result_"+stockcodes[item]+"/result_"+"%d_"%i+stockcodes[item]+"_N.txt")
        Bprofit = NN1.profit(Batch_T, D, Label, Date, Code, "result_"+stockcodes[item]+"/result_"+"%d_"%i+stockcodes[item]+"_B.txt")
        
        if Bprofit[2] != 0:
            f1 = open("result_"+stockcodes[item]+"/result_"+"%d_"%i+stockcodes[item]+"_B.txt", "a")
            f1.write(f"\nAverage Profit: {(Bprofit[1] / Bprofit[2]):.6f} Profit: {Bprofit[1]:.3f} Num: {Bprofit[2]} TEST: {TEST}\n\n")
            f1.close()
        
        if Nprofit[2] != 0 and Bprofit[2] != 0:
            f1 = open("result_"+stockcodes[item]+"/result_"+"%d_"%i+stockcodes[item]+"_N.txt", "a")
            f1.write(f"\nAverage Profit: {(Nprofit[1] / Nprofit[2]):.6f} Profit: {Nprofit[1]:.3f} Num: {Nprofit[2]} TEST: {TEST}\n\n")
            f1.close()
            
            if 1:
                f = open(f"Hypersphere/Hypersphere_{stockcodes[item]}.txt", "a")
                for j in range(len(NN1.W)):
                    f.write("%.6f "%NN1.W[j])
                f.write("\n")
                for j in range(len(D[TEST])):
                    f.write("%.6f "%D[TEST][j])
                f.write("\n")
                print("Nprofit")
                print(Nprofit)
                print(Nprofit[1] / Nprofit[2])
                print("Bprofit")
                print(Bprofit)
                print(Bprofit[1] / Bprofit[2])
                print("TEST")
                print(TEST)
                f.write("%.3f "%Nprofit[1])
                f.write("%d "%Nprofit[2])
                f.write("%d"%TEST)
                f.write("\n\n")
                f.close()
