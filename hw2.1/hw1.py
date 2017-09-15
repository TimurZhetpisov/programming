import urllib.request
import re
new_titles = []
req = urllib.request.Request('http://vechorka.ru/')
with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')
regPostTitle = re.compile('<h1><a href=".*?">.*?</h1>', flags= re.DOTALL)
titles = regPostTitle.findall(html)
regTag = re.compile('<.*?>', re.DOTALL)
regSpace = re.compile('\s{2,}', re.DOTALL)
for t in titles:
    clean_t = regSpace.sub("", t)
    clean_t = regTag.sub("", clean_t)
    new_titles.append(clean_t)
with open('titles.txt', 'w', encoding = 'utf-8') as f:
    for t in new_titles:
        f.write(t+'\n')
