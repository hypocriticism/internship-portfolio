from bs4 import BeautifulSoup
import numpy as np
import urllib.request
import time
import ssl

context = ssl._create_unverified_context()
def Requesting_url(URL):
    t = 0
    while(t < 10):
        e = 100
        try:
            print(URL+" Requesting No.%d" % t)
            webpage = urllib.request.urlopen(URL, context=context)
        except urllib.error.HTTPError:
            t += 1
            time.sleep(0.5)
            e = 400
            pass
        except urllib.error.URLError:
            t += 1
            time.sleep(0.5)
            e = 500
            pass
        except:
            t += 1
            time.sleep(0.5)
            e = 300
            pass
        if(e == 100):
            break
        else:
            print("%d"%e+" Error")
    if(e == 300):
        return e
    else:
        return webpage

def day_parse_append(stockcode, Item, path):
    for item in range(Item):
        SC = str(stockcode[item])
        webpage = Requesting_url("https://finance.naver.com/item/sise_day.nhn?code="+SC+"&page=1")
        if(webpage == 300):
            return 300
        soup = BeautifulSoup(webpage, "html.parser")
        td_num = soup.find_all("td", {"class": "num"})
        td_align = soup.find_all("td", {"align": "center"})
        td_num_string = []
        td_align_string = []
        for i in range(len(td_num)):
            td_num_string.append(td_num[i].get_text())
        for i in range(len(td_align)):
            td_align_string.append(td_align[i].get_text())
        f = open(path+"stockdata_"+SC+".txt", "r", -1, "UTF-8")
        previous = f.readlines()
        previous_day = previous[len(previous) - 1]
        f.close()
        
        f = open(path+"stockdata_"+SC+".txt", "a", -1, "UTF-8")
        for i in range(6):
            if(i % 6 == 0):
                f.write(td_align_string[i // 6])
                f.write(" ")
            if(i % 6 != 1):
                if(td_num_string[i] != 0):
                    f.write(td_num_string[i].replace(",", ""))
                else:
                    f.write(previous_day[i])
                f.write(" ")
            if(i % 6 == 5):
                f.write("\n")
        f.close()
        print(stockcode[item])

f = open("stockcodes.txt", "r")
s = f.read()
stockcodes = s.split()
f.close()

day_parse_append(stockcodes, len(stockcodes), "refined_rev_stockdata_daily/")
