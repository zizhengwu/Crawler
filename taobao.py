#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import urllib2
import json
import re

class Taobao():
    def main(self, url="http://s.taobao.com/search?q=鼠标"):
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)
        for i in soup.select("h3 a"):
            print i["href"]
            print i["title"]
        for i in soup.find_all("div", "price"):
            print i.get_text().strip()

taobao = Taobao()
taobao.main()