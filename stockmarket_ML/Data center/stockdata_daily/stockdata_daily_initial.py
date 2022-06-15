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

def day_parse(stockcode, Item, Page, path):
    for item in range(Item):
        SC = str(stockcode[item])
        f = open(path+"stockdata_"+SC+".txt", "w", -1, "UTF-8")
        f.write("")
        f.close()
        previous_date = 0
            
        for page in range(1, Page + 1):
            webpage = Requesting_url("https://finance.naver.com/item/sise_day.nhn?code="+SC+"&page=%d"%page)
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
                    
            if(previous_date == td_align_string[0]):
                break
            else:
                previous_date = td_align_string[0]
                f = open(path+"stockdata_"+SC+".txt", "a", -1, "UTF-8")
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
        print(stockcode[item])

# Reading stockcodes
f = open("stockcodes.txt", "r")
s = f.read()
stockcodes = s.split()
f.close()

# Parsing function call
day_parse(stockcodes, len(stockcodes), 10, "raw_stockdata_daily/")
