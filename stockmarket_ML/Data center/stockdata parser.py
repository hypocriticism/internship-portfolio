from bs4 import BeautifulSoup
import urllib.request
import ssl
import os
import time

f = open("stockcode.txt", "r")
s = f.read()
stockcodes = s.split()
f.close()

context = ssl._create_unverified_context()

def Requesting_url(page, SC):
    t = 0
    e = 100
    while(t < 10):
        try:
            print("stockdata_"+SC+" page: %d" % page+" Requesting No.%d" % t)
            webpage = urllib.request.urlopen("https://finance.naver.com/item/sise_day.nhn?code="+SC+"&page=%d"%page, context=context)
        except urllib.error.URLError as e:
            t += 1
            time.sleep(0.5)
            pass
        if(e < 300):
            break
        else:
            print("%d"%e+" Error")
    return webpage

for stockcode in range(len(stockcodes)):
    SC = str(stockcodes[stockcode])
    f = open("stockdata/stockdata_"+SC+".txt", "w", -1, "UTF-8")
    f.write("")
    f.close()

    for page in range(1, 51):
        webpage = Requesting_url(page, SC)

        soup = BeautifulSoup(webpage, "html.parser")
        td_num = soup.find_all("td", {"class": "num"})
        td_align = soup.find_all("td", {"align": "center"})
        td_num_string = []
        td_align_string = []
        for i in range(len(td_num)):
            td_num_string.append(td_num[i].get_text())
        for i in range(len(td_align)):
            td_align_string.append(td_align[i].get_text())


        f = open("stockdata/stockdata_"+SC+".txt", "a", -1, "UTF-8")
        for i in range(len(td_num_string)):
            if(i % 6 == 0):
                f.write(td_align_string[i // 6])
                f.write(" ")
            if(i % 6 != 1):
                f.write(td_num_string[i].replace(",", ""))
                f.write(" ")
            if(i % 6 == 5):
                f.write("\n")
        f.close()
    print(stockcodes[stockcode])
