#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import urllib2
import json
import re

class Amazon():
    def main(self, url="http://www.amazon.cn/s/ref=nb_sb_noss_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=%E9%BC%A0%E6%A0%87"):
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)
        for i in soup.find_all(lambda tag: tag.name == "div" and tag.get("class") == ['productTitle']):
            print i.find("a")["href"].strip()
            print i.get_text().strip()
            # print i["href"]
            # print i.get_text().strip()
        for i in soup.find_all("div", "newPrice"):
            print i.find("span").get_text().strip()

amazon = Amazon()
amazon.main()