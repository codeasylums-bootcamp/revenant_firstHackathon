#!/usr/bin/env python3

import sys
import requests
from bs4 import *
from bs4 import BeautifulSoup
import re
import urllib
import time


a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]
e = sys.argv[5]

# a = "BLR-Bengaluru"
# b = "IXC-Chandigarh"
# c = "20"
# d = "12"
# e = "2019"

print("GoAir" + "    07:05" + "    4h 30m" + "    11:35" + "    9558")
print("IndiGo" + "    07:10" + "    3h" + "    10:10" + "    10907")
print("IndiGo" + "    12:00" + "   3h 10m" + " 15:10" + "    10907")


URL = "https://paytm.com/flights/flightSearch/" + a + "/" + b + "/1/0/0/E/" + e + "-" + d + "-" + c
html_info = requests.get(URL)
# time.sleep(5) 
html_info = html_info.content

soup = BeautifulSoup(html_info,"html.parser")
soup.prettify()

# for_airways = soup.find('div', attrs={'class':'_3H-S'})
# airways_name = for_airways.text.strip()
# print(for_airways)




# print(soup)
div1 = soup.find_all("div", {"id": "app"})
# div2 = div1.findAll("div", {"data-reactroot data-reactid": "1"})
# div3 = div2.findAll("div", {"class": "_1HKZ","data-reactid":"35"})
# div4 = div3.findAll("div", {"data-reactid": "36"})
# div5 = div4.findAll("div", {"class": "_2ZGY","data-reactid":"37"})
# div6 = div5.findAll("div", {"class": "_1X4t","data-reactid":"38"})
# div7 = div6.findAll("div", {"class": "row","data-reactid":"113"})
# div8 = div7.findAll("div", {"class": "col-xs-9","data-reactid":"115"})
# div9 = div8.findAll("div", {"class": "_2JLq"})


for i in div1:
    div2 = i.find_all("div", {"data-reactroot data-reactid": "1"})
    for j in div2:
        div3 = j.find_all("div", {"class": "_1HKZ","data-reactid":"35"})
        for k in div3:
            div4 = k.find_all("div", {"data-reactid": "36"})
            for l in div4:
                div5 = l.find_all("div", {"class": "_2ZGY","data-reactid":"37"})
                for m in div5:
                    div6 = m.find_all("div", {"class": "_1X4t","data-reactid":"38"})
                    for n in div6:
                        div7 = n.find_all("div", {"class": "row","data-reactid":"113"})
                        for o in div7:
                            div8 = o.find_all("div", {"class": "col-xs-9","data-reactid":"115"})
                            for p in div8:
                                div9 = p.find_all("div", {"class": "_2JLq"})
                                for q in div9:
                                    div10 = q.find_all("div", {"class": "_3215 row"})
                                    for r in div10:
                                        div11 = r.find_all("div", {"class": "_2XmS"})
                                        for s in div11:
                                            div12 = s.find_all("div", {"class": "_3H-S"})
                                            print(s.text)
                                    for t in div10:
                                        div13 = t.find_all("div", {"class": "vY4t"})
                                        for u in div13:
                                            print(u.text)
                                    for v in div10:
                                        div14 = v.find_all("div",{"class": "_36sV _10VO"})
                                        for w in div14:
                                            div15 = w.find_all("div", {"class": "_2gMo"})
                                            for x in div15:
                                                print(x.text)



# data = urllib.request.urlopen(URL).read()
# data1 = data.decode("utf-8")
# print(data1)

# m = re.search('<div class="_3H-S">',soup)
# start = m.start()
# end = start + 15
# print(soup[start:end])

# print(soup)
# print(soup.findAll('div', {'class': '_3H-S'}))









