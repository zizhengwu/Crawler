#!C:/Python27/python
#-*-coding:utf-8-*-
from os import *  
import cgi
from bs4 import BeautifulSoup
import urllib2
import json
import re

class Taobao():
    def main(self):
        fs = cgi.FieldStorage()
        names = []
        links = []
        prices = []
        srcs = []
        data = []
        url = "http://s.taobao.com/search?q="+fs["keyword"].value
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)
        for i in soup.select("h3 a"):
            links.append(i["href"])
            names.append(i["title"])
        for i in soup.find_all("div", "price"):
            prices.append(i.get_text().strip())
        for i in soup.findAll(attrs={"data-ks-lazyload" : re.compile(".*")}):
            srcs.append(i["data-ks-lazyload"])
        data.append(names)
        data.append(links)
        data.append(prices)
        data.append(srcs)
        print "Content-type: application/json\n"
        print json.dumps(data)
taobao = Taobao()
taobao.main()