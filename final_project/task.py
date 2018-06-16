import gensim
import pymorphy2
import requests
import datetime
import os
import math
from tqdm import tqdm

LINKS_PATH = "links.txt"
FOLDER = "posts"
N = 10
TOKEN = 'a69fabcba69fabcba69fabcb13a6fb79bdaa69fa69fabcbfdbad967e6fb182c4f5b230a'
stuff = '[\.\?!"@№;%:?*_()-+=#$^&:;\'"><,/\|\\~`]'
path = 'links.txt'
u_start = datetime.datetime(2018, 6, 13, hour=3).timestamp()
u_finish = datetime.datetime(2018, 6, 15, hour=3).timestamp()


def number(link):
    r = requests.get(link).json()
    number = r['response']['count']
    return number


def datas(link):
    return requests.get(link).json()


def linksToList(path):
    links = []
    f = open(path)
    for line in f.readlines():
        links.append(line.splitlines())
    return links


def main():
    if not os.path.exists("posts"):
        os.makedirs("posts")

    domains = linksToList(path)
    saveallposts(domains)
    findallkeys(domains)


def saveallposts(domains):
    for domain in domains:
        saveposts(domain)


def findallkeys(domains):
    for domain in domains:
        findkeys(domain)


def findkeys(domain):
    n_words = {}
    with open('posts/' + ''.join(domain) + '.txt', 'r') as handle:
        text = handle.read()
    words = gensim.utils.simple_tokenize(text)
    morph = pymorphy2.MorphAnalyzer()
    for word in tqdm(words):
        if len(word) > 3:
            p = morph.parse(word)[0]
            normal_word = p.normal_form
            n_words[normal_word] = n_words.get(normal_word, 0) + 1
            i = N
    with open(''.join(domain) + 'keys.txt', 'w') as f:
        for word in sorted(n_words, key=n_words.get, reverse=True):
            if i > 0:
                f.write(word + '\n')
                i -= 1


def saveposts(domain):
    domain = ''.join(domain)
    link = 'https://api.vk.com/method/wall.get?domain=' + domain + '&&count=1&offset=0&v=5.73&access_token=' + TOKEN
    p_number = number(link)
    h = math.ceil(p_number / 100)
    o = 0
    s = 100
    for i in range(0, h):
        if i <= 100:
            link = 'https://api.vk.com/method/wall.get?domain=' + domain + '&&count=100&offset=' + str(
                o) + '&v=5.73&access_token=' + TOKEN
            data = datas(link)
            if not os.path.exists(FOLDER):
                os.makedirs(FOLDER)
            if p_number <= 100:
                for k in range(0, p_number):
                    text = data['response']['items'][k]['text']
                    date = data['response']['items'][k]['date']
                    with open(FOLDER + '/' + domain + '.txt', 'a', encoding='utf-8') as m:
                        print('11')
                        if u_start <= int(date) <= u_finish:
                            print('1')
                            m.write(text + ' ')

            else:
                for k in range(0, 100):
                    text = data['response']['items'][k]['text']
                    date = data['response']['items'][k]['date']
                    with open(FOLDER + '/' + domain + '.txt', 'a', encoding='utf-8') as m:
                        print('22')
                        if u_start <= int(date) <= u_finish:
                            print('2')
                            m.write(text + ' ')
                p_number = p_number - s
                o = o + 100


if __name__ == '__main__':
    main()
