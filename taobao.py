#!C:/Python27/python
#-*-coding:utf-8-*-
from os import *  
from cgi import *
from bs4 import BeautifulSoup
import urllib2
import json
import re

class Taobao():
    def main(self, url="http://s.taobao.com/search?q=鼠标"):
        names = []
        links = []
        prices = []
        data = []
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)
        for i in soup.select("h3 a"):
            links.append(i["href"])
            names.append(i["title"])
        for i in soup.find_all("div", "price"):
            prices.append(i.get_text().strip())
        data.append(names)
        data.append(links)
        data.append(prices)
        print "Content-type: application/json\n"
        print json.dumps(data)
taobao = Taobao()
taobao.main()