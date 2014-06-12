from bs4 import BeautifulSoup
import urllib2
import re
class Main():
    def process(self):
        items = set()
        page = urllib2.urlopen('http://search.jd.com/Search?keyword=%E5%86%85%E5%AD%98&enc=utf-8')
        soup = BeautifulSoup(page)
        pat = re.compile(r'href="([^"]*)"')
        for i in soup.find_all(href=re.compile("item.*html$"), target="_blank"):
            h = pat.search(str(i))
            href = h.group(1)
            items.add(href)
        for i in items:
            print i
main = Main()
main.process()