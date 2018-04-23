import urllib.request
import json
import os
import math
import re
import matplotlib.pyplot as plt
kek = '[\.\?!"@№;%:?*_()-+=#$^&:;\'"><,/\|\\~`]'
def main():
    makedirs()
    makegraphs()
def makedirs():
    os.mkdir('data')
    os.mkdir('data/posts/')
    os.mkdir('data/comments/')
def posts():
    kek = '[\.\?!"@№;%:?*_()-+=#$^&:;\'"><,/\|\\~`]'
    u_ids = []
    p_len = []
    p_ids = []
    p_num = num('https://api.vk.com/method/wall.get?owner_id=-29534144&count=1&offset=0&v=5.73&access_token=96be881a96be881a96be881aaf96dcb999996be96be881acc7d97106457a3fa5bc08bf8')
    h = math.ceil(p_num/100)
    o = 0
    s = 100
    for i in range(0, h):
        if i <= 100: 
            link = 'https://api.vk.com/method/wall.get?owner_id=-29534144&count=100&offset=' + str(o) + '&v=5.73&access_token=96be881a96be881a96be881aaf96dcb999996be96be881acc7d97106457a3fa5bc08bf8'
            data, result = datas(link)
            if p_num <= 100:
                for k in range(0, p_num): 
                    text = data['response']['items'][k]['text']
                    with open ('data/posts/post ' + str(k + i*100 + 1) + '.txt', 'w', encoding = 'utf-8') as x:
                        x.write(text)
                    if re.search(kek, text):
                        text = re.sub(kek, "", text)
                    if text == '\s*':
                        p_len.append(0)
                    else:
                        words = text.split()
                        p_len.append(len(words))
                    u_id = str(data['response']['items'][k]['from_id'])
                    u_ids.append(u_id)     
                    p_id = data['response']['items'][k]['id']
                    p_ids.append(p_id) 
            else:
                for k in range(0, 100): 
                    text = data['response']['items'][k]['text']
                    with open ('data/posts/post ' + str(k + i*100 + 1) + '.txt', 'w', encoding = 'utf-8') as x:
                        x.write(text)
                    if re.search(kek, text):
                        text = re.sub(kek, "", text)
                    if text == '\s*':
                        p_len.append(0)
                    else:
                        words = text.split()
                        p_len.append(len(words))
                    p_id = data['response']['items'][k]['id']                
                    p_ids.append(p_id) 
                    u_id = str(data['response']['items'][k]['from_id'])
                    u_ids.append(u_id)
                p_num = p_num - s
                o = o + 100
    return p_ids, p_len, u_ids
def comm():
    ucom_ids = []
    len_c = []
    len_everyc = []
    c_nums = []
    p_ids, p_len, u_ids = posts()
    s = 100
    o = 0
    com = ''
    for i in range(len(p_ids)):
        n = 0
        p = 0
        link = 'https://api.vk.com/method/wall.getComments?owner_id=-29534144&post_id=' + str(p_ids[i]) + '&count=100&v=5.73&access_token=96be881a96be881a96be881aaf96dcb999996be96be881acc7d97106457a3fa5bc08bf8'
        c_num = num(link)
        c_nums.append(c_num) 
        if c_num != 0:
            h = math.ceil(c_num/100)
            for j in range(0, h):
                link = 'https://api.vk.com/method/wall.getComments?owner_id=-29534144&post_id=' + str(p_ids[i]) + '&offset=' + str(o) + '&count=100&v=5.73&access_token=96be881a96be881a96be881aaf96dcb999996be96be881acc7d97106457a3fa5bc08bf8'
                data, result = datas(link)
                if c_num <= 100:
                    for k in range(0, c_num):
                        h = 0
                        words = data['response']['items'][k]['text']
                        ucom_id = str(data['response']['items'][k]['from_id'])
                        ucom_ids.append(ucom_id) 
                        if re.search(kek, words):
                            words = re.sub(kek, "", words)
                        words_new = words.split()
                        if len(words_new) != 0:
                            l = len(words_new)
                            len_everyc.append(l)
                        else:
                            len_everyc.append(0)
                        n = n + len(words)
                        p = p + 1
                        comm = comm + data['response']['items'][k]['text'] + '\n'
                    with open ('data/comments/comments for post ' + str(i + 1) + '.txt', 'w', encoding = 'utf-8') as x:
                        x.write(comm)
                    len_c.append(n/p)
                else:
                    for k in range(0, 100):
                        h = 0
                        words = data['response']['items'][k]['text']
                        ucom_id = str(data['response']['items'][k]['from_id'])
                        ucom_ids.append(ucom_id) 
                        if re.search(kek, words):
                            words = re.sub(kek, "", words)
                        words = words.split()
                        if len(words_new) != 0:
                            h = len(words_new)
                            len_everyc.append(h)
                        else:
                            len_everyc.append(0)
                        n = n + len(words)
                        p = p + 1
                        comm = comm + data['response']['items'][k]['text'] + '\n'
                    with open ('data/comments/comments for post ' + str(i + 1) + '.txt', 'w', encoding = 'utf-8') as x:
                        x.write(comm)
                    c_len.append(n/p)
                    с_num = с_num - s
                    o = o + 100
        else:
            with open ('data/comments/comments for post ' + str(i + 1) + '.txt', 'w', encoding = 'utf-8') as x:
                x.write('')
            c_len.append(n)
        comm = ''
    return c_len, everyc_len, ucom_ids
def num(link):
    req = urllib.request.Request(link)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8', errors = 'ignore')
    data = json.loads(result)
    num = data['response']['count']
    return num
def datas(link):
    req = urllib.request.Request(link)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8', errors = 'ignore')
    data = json.loads(result)
    return data, result    
def com():
    ucom_ids = []
    len_c = []
    len_everyc = []
    c_num = []
    p_ids, p_len, u_ids = posts()
    s = 100
    o = 0
    com = ''
    for i in range(len(p_ids)):
        n = 0
        p = 0
        link = 'https://api.vk.com/method/wall.getComments?owner_id=-29534144&post_id=' + str(p_ids[i]) + '&count=100&v=5.73&access_token=96be881a96be881a96be881aaf96dcb999996be96be881acc7d97106457a3fa5bc08bf8'
        c_num = num(link)
        c_num.append(c_num) 
        if c_num != 0:
            h = math.ceil(c_num/100)
            for j in range(0, h):
                link = 'https://api.vk.com/method/wall.getComments?owner_id=-29534144&post_id=' + str(p_ids[i]) + '&offset=' + str(o) + '&count=100&v=5.73&access_token=96be881a96be881a96be881aaf96dcb999996be96be881acc7d97106457a3fa5bc08bf8'
                data, result = datas(link)
                if c_num <= 100:
                    for k in range(0, c_num):
                        h = 0
                        words = data['response']['items'][k]['text']
                        ucom_id = str(data['response']['items'][k]['from_id'])
                        ucom_ids.append(ucom_id) 
                        if re.search(kek, words):
                            words = re.sub(kek, "", words)
                        words_new = words.split()
                        if len(words_new) != 0:
                            l = len(words_new)
                            len_everyc.append(l)
                        else:
                            len_everyc.append(0)
                        n = n + len(words)
                        p = p + 1
                        comm = comm + data['response']['items'][k]['text'] + '\n'
                    with open ('data/comments/comments for post ' + str(i + 1) + '.txt', 'w', encoding = 'utf-8') as x:
                        x.write(comm)
                    len_c.append(n/p)
                else:
                    for k in range(0, 100):
                        h = 0
                        words = data['response']['items'][k]['text']
                        ucom_id = str(data['response']['items'][k]['from_id'])
                        ucom_ids.append(ucom_id) 
                        if re.search(kek, words):
                            words = re.sub(kek, "", words)
                        words = words.split()
                        if len(words_new) != 0:
                            h = len(words_new)
                            len_everyc.append(h)
                        else:
                            len_everyc.append(0)
                        n = n + len(words)
                        p = p + 1
                        comm = comm + data['response']['items'][k]['text'] + '\n'
                    with open ('data/comments/comments for post ' + str(i + 1) + '.txt', 'w', encoding = 'utf-8') as x:
                        x.write(comm)
                    c_len.append(n/p)
                    с_num = с_num - s
                    o = o + 100
        else:
            with open ('data/comments/comments for post ' + str(i + 1) + '.txt', 'w', encoding = 'utf-8') as x:
                x.write('')
            c_len.append(n)
        comm = ''
    return c_len, everyc_len, ucom_ids
def users(length, u_ids):
    cities = []
    ages = []
    for i in range(len(u_ids)):
        if f_ids[i].startswith( '-' ) == False:
            link = 'https://api.vk.com/method/users.get?user_ids=' + f_ids[i] + '&fields=bdate,city,home_town&v=5.73&access_token=96be881a96be881a96be881aaf96dcb999996be96be881acc7d97106457a3fa5bc08bf8'
            data, result = datas(link)
            if re.search('bdate', result):
                bdate = data['response'][0]['bdate']
                if re.search('\d+\.\d+.(\d+)', bdate):
                    year = re.search('\d+\.\d+.(\d+)', bdate).group(1)
                    age = 2018-int(year)
                    ages.append(age)
                else:
                    ages.append('')
            else:
                ages.append('')
            if re.search('home_town', result):
                city = data['response'][0]['home_town']
                cities.append(city)
            else:
                if re.search('city', result):
                    city = data['response'][0]['city']['title']
                    cities.append(city)
                else:
                    cities.append('')
        else:
            ages.append('')
            cities.append('')
    return ages, cities
def post_id():
    length = []
    p_ids, length, u_ids = posts()
    cities = []
    ages = []
    ages, cities = users(length, u_ids)
    return ages, cities, length
def comm_id():
    length = []
    length_c, length, u_ids = comm()
    towns = []
    ages = []
    ages, cities = users(length, u_ids)
    return ages, cities, length   
def for_graph(x, y):
    arr = []
    lenn = []
    for a in range(len(x)):
        if (x[a] not in arr) and (x[a] != ''):
            arr.append(x[a])
            k = 1
            n = int(y[a])
            for f in range(len(x)):
                if (x[f] in arr) and (f != a):
                    k = k + 1
                    n = n + int(y[f])
            lenn.append(n/k)
    return(arr, lenn)
def for_post_comm_graph():
    d, len_p, g = posts()
    len_c, s, f = comm()
    x, y = for_graph(len_p, len_c)
    return x,y
def for_comm_age_graph():
    ages = []
    length = []
    ages, towns, length = comm_users()
    x, y = for_graph(ages, length)
    return x,y
def for_com_cities_graph():
    towns = []
    length = []
    ages, towns, length = comm_users()
    x, y = for_graph(towns, length)
    return x,y
def for_post_age_graph():
    ages = []
    length = []
    ages, cities, length = post_users()
    x, y = for_graph(ages, length)
    return x,y
def for_post_cities_graph():
    towns = []
    length = []
    ages, cities, length = post_users()
    x, y = for_graph(cities, length)
    return x,y
def graph(x, y, title, xname, yname):
    plt.plot(x, y, color='blue')
    plt.scatter(x, y)
    plt.title(title)
    plt.ylabel(xname)
    plt.xlabel(yname)
    plt.show()
def post_comm_graph():
    x = []
    y = []
    x, y = for_post_comm_graph()
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                a = x[j]
                b = x[j+1]
                d = y[j]
                e = y[j+1]
                x[j] = b  
                x[j+1] = a
                y[j] = e
                y[j+1] = d
        for j in range(len(x)-1, 0, -1):
            if x[j-1] > x[j]:
                a = x[j]
                b = x[j-1]
                d = y[j]
                e = y[j-1]
                x[j] = b
                x[j-1] = a
                y[j] = e
                y[j-1] = d
    title = 'Длина поста/ средняя длина комментария'
    xname = 'Средняя длина комментариев'
    yname = 'Длина поста'
    graph(x, y, title, xname, yname)
def comm_age_graph():
    x = []
    y = []
    x, y = for_comm_age_graph()
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                a = x[j]
                b = x[j+1]
                d = y[j]
                e = y[j+1]
                x[j] = b  
                x[j+1] = a
                y[j] = e
                y[j+1] = d
        for j in range(len(x)-1, 0, -1):
            if x[j-1] > x[j]:
                a = x[j]
                b = x[j-1]
                d = y[j]
                e = y[j-1]
                x[j] = b
                x[j-1] = a
                y[j] = e
                y[j-1] = d
    title = 'Средняя длина комментария/возраст'
    xname = 'Длина комментария'
    yname = 'Возраст'
    graph(x, y, title, xname, yname)
def post_age_graph():
    x = []
    y = []
    x, y = for_post_age_graph()
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                a = x[j]
                b = x[j+1]
                d = y[j]
                e = y[j+1]
                x[j] = b  
                x[j+1] = a
                y[j] = e
                y[j+1] = d
        for j in range(len(x)-1, 0, -1):
            if x[j-1] > x[j]:
                a = x[j]
                b = x[j-1]
                d = y[j]
                e = y[j-1]
                x[j] = b
                x[j-1] = a
                y[j] = e
                y[j-1] = d
    title = 'Средняя длина поста/возраст'
    xname = 'Длина поста'
    yname = 'Возраст'
    graph(x, y, title, xname, yname)
def comm_cities_graph():
    x = []
    y = []
    xnumb = []
    x, y = for_comm_cities_graph()
    for i in range(len(x)):
        xnumb.append(i)
    title = 'Средняя длина комментария/город'
    xname = 'Длина комментария'
    yname = 'Город'
    plt.xticks(xnumb, x)
    graph(xnumb, y, title, xname, yname)
def post_cities_graph():
    x = []
    y = []
    xnumb = []
    x, y = for_post_towns_graph()
    for i in range(len(x)):
        xnumb.append(i)
    title = 'Средняя длина поста/орода'
    xname = 'Длина поста'
    yname = 'Город'
    plt.xticks(xnumb, x)
    graph(xnumb, y, title, xname, yname)
def makegraphs():
    post_comm_graph()
    comm_age_graph()
    comm_cities_graph()
    post_age_graph()
    post_cities_graph()
    
if __name__ == '__main__':
    main()
