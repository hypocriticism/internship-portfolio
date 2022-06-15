# Reading stockcodes
f = open("stockcodes.txt", "r")
s = f.read()
stockcodes = s.split()
f.close()

# Main loop
for i in range(len(stockcodes)):
    # Par value division
    div = 1
    
    # Reading raw stockdata
    f = open("raw_stockdata/stockdata_"+stockcodes[i]+".txt", "r", -1, "UTF-8")
    s = f.read()
    stockdata = s.split()

    # Str to Int
    for j in range(len(stockdata)):
        if(j % 6 != 0):
            stockdata[j] = int(stockdata[j])

    # Appending refined stockdata
    new_stockdata = []
    for j in range(len(stockdata)):
        if(j % 6 == 0):
            new_stockdata.append(stockdata[j])
            
        if(j % 6 == 1):
            if(stockdata[j] != 0):
                if(j > 6):
                    if(stockdata[j - 6] / stockdata[j] > 1.3 or stockdata[j - 6] / stockdata[j] < 0.7 and stockdata[j + 4] == 0):
                        if(stockdata[j - 6 + 1] != 0):
                            div *= stockdata[j - 6 + 1] / stockdata[j]
                        else:
                            div *= stockdata[j - 6] / stockdata[j]
                new_stockdata.append(stockdata[j] * div)
            else:
                k = j
                while(k < len(stockdata) and stockdata[k] != 0):
                    k += 6
                if(k < len(stockdata)):
                    new_stockdata.append(stockdata[k] * div)
                elif(j > 6):
                    new_stockdata.append(new_stockdata[j - 6])
                else:
                    new_stockdata.append(stockdata[j])
                    
        if(j % 6 == 2 or j % 6 == 3 or j % 6 == 4):
            if(stockdata[j] != 0):
                new_stockdata.append(stockdata[j] * div)
            else:
                new_stockdata.append(stockdata[j // 6 * 6 + 1] * div)
                
        if(j % 6 == 5):
            new_stockdata.append(stockdata[j] // div)
    f.close()

    # Writing refined stockdata
    f = open("refined_stockdata/stockdata_"+stockcodes[i]+".txt", "w")
    for j in range(len(new_stockdata)):
        if(j % 6 != 0):
            f.write("%d"%int(new_stockdata[j]))
        else:
            f.write(new_stockdata[j])
        if(j % 6 == 5):
            f.write("\n")
        else:
            f.write(" ")
    f.close()

    # Error check
    f = open("refined_stockdata/stockdata_"+stockcodes[i]+".txt", "r")
    s = f.read()
    test_stockdata = s.split()
    for j in range(len(test_stockdata)):
        if(j % 6 != 0):
            if(j > 6 and j % 6 != 5):
                if(round(int(test_stockdata[j - 6]) / int(test_stockdata[j])) >= 10 or round(int(test_stockdata[j]) / int(test_stockdata[j - 6])) >= 10):
                    print(stockcodes[i], test_stockdata[(j // 6) * 6])
            if(int(test_stockdata[j]) == 0 and j % 6 != 5):
                print(stockcodes[i], test_stockdata[(j // 6) * 6])
    f.close()
    
