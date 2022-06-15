import math

def movingaverage(P, loc, N):
    avg = 0
    for i in range(N):
        avg += P[loc - i] / N
    return avg

def local_Maximum(H, loc, N):
    M = 0
    for i in range(N):
        if(H[loc - i] > M):
            M = H[loc - i]
    return M

def local_Minimum(L, loc, N):
    m = 10**10
    for i in range(N):
        if(L[loc - i] < m and L[loc - i] != 0):
            m = L[loc - i]
    return m

# Reading stockcodes
f = open("stockcodes.txt", "r")
s = f.read()
stockcodes = s.split()
f.close()

# Define range and opening files
N = 500
f1 = open("Label.txt", "w")
f2 = open("Phasespace.txt", "w")

# Main loop
for i in range(len(stockcodes)):
    f = open("refined_stockdata/stockdata_"+stockcodes[i]+".txt", "r")
    s = f.readlines()
    f.close()
    
    Date = []
    P = []
    S = []
    H = []
    L = []
    T = []

    # Data loop
    for j in range(min(len(s), N)):
        ss = s[j].split()
        Date.append(ss[0])
        P.append(int(ss[1]))
        S.append(int(ss[2]))
        H.append(int(ss[3]))
        L.append(int(ss[4]))
        T.append(int(ss[5]))

    # Dimension loop
    for j in range(1, min(len(s), N) - 100):
        DD = []

        # Dimensions Begin
        DD.append(math.log(T[j] + 1) + math.log(P[j]))
        DD.append(math.log(T[j] + 1) - math.log(T[j + 1] + 1))

        DD.append((movingaverage(P, j + 60, 30) / movingaverage(P, j + 100, 50) - 1) * 100)
        DD.append((movingaverage(P, j + 30, 15) / movingaverage(P, j + 60, 30) - 1) * 100)
        DD.append((movingaverage(P, j + 20, 10) / movingaverage(P, j + 30, 15) - 1) * 100)
        DD.append((movingaverage(P, j + 10, 5) / movingaverage(P, j + 20, 10) - 1) * 100)
        DD.append((P[j + 5] / movingaverage(P, j + 10, 5) - 1) * 100)

        DD.append((P[j + 4] / P[j + 5] - 1) * 100)
        DD.append((P[j + 3] / P[j + 4] - 1) * 100)
        DD.append((P[j + 2] / P[j + 3] - 1) * 100)
        DD.append((P[j + 1] / P[j + 2] - 1) * 100)
        DD.append((P[j] / P[j + 1] - 1) * 100)

        DD.append((P[j + 4] / S[j + 4] - 1) * 100)
        DD.append((P[j + 3] / S[j + 3] - 1) * 100)
        DD.append((P[j + 2] / S[j + 2] - 1) * 100)
        DD.append((P[j + 1] / S[j + 1] - 1) * 100)
        DD.append((P[j] / S[j] - 1) * 100)

        DD.append((S[j - 1] / P[j] - 1) * 100)

        DD.append((P[j] / local_Maximum(H, j + 100, 100)) * 100)
        DD.append((P[j] / local_Maximum(H, j + 60, 60)) * 100)
        DD.append((P[j] / local_Maximum(H, j + 30, 30)) * 100)
        DD.append((P[j] / local_Maximum(H, j + 20, 20)) * 100)
        DD.append((P[j] / local_Maximum(H, j + 10, 10)) * 100)
        DD.append((P[j] / local_Maximum(H, j + 5, 5)) * 100)

        DD.append((P[j] / local_Minimum(L, j + 100, 100)) * 100)
        DD.append((P[j] / local_Minimum(L, j + 60, 60)) * 100)
        DD.append((P[j] / local_Minimum(L, j + 30, 30)) * 100)
        DD.append((P[j] / local_Minimum(L, j + 20, 20)) * 100)
        DD.append((P[j] / local_Minimum(L, j + 10, 10)) * 100)
        DD.append((P[j] / local_Minimum(L, j + 5, 5)) * 100)
        # Dimensions End

        # Labels
        f1.write("["+stockcodes[i]+", "+Date[j]+"]")
        f1.write(" ")
        f1.write("%.2f"%((P[j - 1] / S[j - 1] - 1) * 100 - 0.33))
        f1.write("\n")

        # Phasespace
        f2.write("["+stockcodes[i]+", "+Date[j]+"]")
        f2.write(" ")
        for k in range(len(DD)):
            f2.write("%.8f "%DD[k])
        f2.write("\n")
        
    print(stockcodes[i])
    
f1.close()
f2.close()
