import urllib.request
import re

names = ['path', 'author', 'sex', 'birthday', 'header', 'created', 'sphere', 'genre_fi', 'type', 'topic', 'chronotop',
         'style', 'audience_age', 'audience_level', 'audience_size', 'source', 'publication', 'publisher', 'publ_year',
         'medium', 'country', 'region', 'language']


def generate_links():
    base = 'http://vechorka.ru/rubrics/russia/news/'
    res = []
    for i in range(1, 45):
        page_link = base + str(i)
        try:
            page_text = urllib.request.urlopen(page_link).read().decode('utf-8')
            page_news_links = get_local_links(page_text)
            for elem in page_news_links:
                res.append(elem)
        except:
            print('Error generation')
    return res


def get_local_links(text):
    arr = re.findall('<h3><a href="(.*)">', text)
    res = []
    base = 'http://vechorka.ru'
    for elem in arr:
        res.append(base + elem)
    return res


def get_page_text(link):
    text = None
    try:
        data = urllib.request.urlopen(link)
        text = data.read().decode('utf-8')
    except:
        print('Error download')
    return text


def get_metadata(text, link):
    global links
    print(links.index(link), ' of ', len(links))
    general_dict = dict()
    for elem in names:
        date = ''
        if elem in ['sex', 'birthday', 'genre_fi', 'type', 'chronotop', 'publisher']:
            general_dict[elem] = ''
        elif elem == 'sphere':
            general_dict[elem] = 'публицистика'
        elif elem == 'style':
            general_dict[elem] = 'нейтральный'
        elif elem == 'audience_age':
            general_dict[elem] = 'н-возраст'
        elif elem == 'audience_level':
            general_dict[elem] = 'н-уровень'
        elif elem == 'audience_size':
            general_dict[elem] = 'городская'
        elif elem == 'publication':
            general_dict[elem] = 'Вечерний Ставрополь'
        elif elem == 'medium':
            general_dict[elem] = 'газета'
        elif elem == 'country':
            general_dict[elem] = 'Россия'
        elif elem == 'region':
            general_dict[elem] = 'Ставропольский край'
        elif elem == 'language':
            general_dict[elem] = 'ru'
        elif elem == 'path':
            general_dict[elem] = ''
        elif elem == 'author':
            general_dict[elem] = ''
        elif elem == 'header':
            head = re.findall('<title>(.*)</title>', text)
            general_dict[elem] = head[0]
        elif elem == 'created':
            date = re.findall('datetime="(.*)T', text)
            date = date[0].split('-')
            date = reversed(date)
            date = '.'.join(date)
            general_dict[elem] = date
        elif elem == 'topic':
            general_dict[elem] = ''
            tags = re.findall('<span class="icon14 tags"><a href="/tags/(.*)</a></span> ', text)
            tags = tags[0].split('</a>, <a href="/tags/')
            for i, elem in enumerate(tags):
                tags[i] = elem.split('>')[1]
            general_dict[elem] = ', '.join(tags)
        elif elem == 'source':
            general_dict[elem] = link
        elif elem == 'publ_year':
            general_dict[elem] = date.split('-')[-1]
    res = []
    for elem in names:
        res.append(general_dict[elem])
    return '\t'.join(res), general_dict


def main():
    global links
    links = generate_links()
    csv_data = ['\t'.join(names)]
    for link in links:
        text = get_page_text(link)
        if text:
            try:
                metadata, dict_meta = get_metadata(text, link)
                csv_data.append(metadata)
            except:
                pass
    csv = open('metadata.csv', 'w')
    csv.write('\n'.join(csv_data))
    csv.close()

main()
