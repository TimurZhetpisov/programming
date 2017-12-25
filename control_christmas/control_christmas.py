import json
import os
import re
from bs4 import BeautifulSoup
def crawl():
    d = {}
    lst = os.listdir('thai_pages') #та же папка
    for fl in lst:
        with open('thai_pages/'+fl, 'r', encoding='utf-8') as f:
            html = f.read()
            d.update(get_dict(html))
    return d
def get_dict(html):
    d = {}
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    tr_items = soup.find_all('tr')
    for it in tr_items:
        trs = it.find_all('td')
        if trs:
            w = trs[0].find('a')
            if w:
                w = w.get_text()
                d[w] = trs[-1].get_text()
    return d
def jsonify(d):
    text = json.dumps(d)
    with open('thai-eng.json', 'w', encoding='utf-8') as f:
        f.write(text)
    inv_d = {v: k for k, v in d.items()}
    new_inv_d = {}
    for key in inv_d:
        if ';' in key:
            keys = key.split(';')
            for k in keys:
                new_inv_d[k] = inv_d[key]
    inv_d.update(new_inv_d)
    text_i = json.dumps(inv_d)
    with open('eng-thai.json', 'w', encoding='utf-8') as f:
        f.write(text_i) 
def main():
    d = crawl()
    jsonify(d)
if __name__ == '__main__':
    main()
