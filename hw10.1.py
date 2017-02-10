import re
def search1():
    with open('plant.html', 'r', encoding = 'utf-8') as f:
        found = []
        article = f.read()
        f.close()
        result2 = re.findall(r'Семейство:\&nbsp;<\/td>\n<td width="60%" align="left"><a href="https:\/\/ru\.wikipedia\.org\/wiki\/.+" class="mw-redirect" title=".+">.+<\/a><\/td>', article)
        print(result2)
search1()
