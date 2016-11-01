import re
import time
from bs4 import BeautifulSoup
from lxml import html as lxmlhtml
import requests

def timeit(fn, *args):
    t1 = time.time()
    for i in range(100):
        fn(*args)
    t2 = time.time()
    print('%s took %0.3f ms' % (fn.func_name, (t2-t1)*1000.0))
    
def bs_test(html):
    soup = BeautifulSoup(html,'html.parser')
    return soup.html.head.title
    
def lxml_test(html):
    tree = lxmlhtml.fromstring(html)
    return tree.xpath('//title')[0].text_content()
    
def regex_test(html):
    return re.findall('title', html)[0]
    
if __name__ == '__main__':
    url = 'http://pycon.org'
    html = requests.get(url).text
    for fn in (bs_test, lxml_test, regex_test):
        timeit(fn, html)