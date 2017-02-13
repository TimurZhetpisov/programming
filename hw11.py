import re
def replace():
    with open('dino.html', 'r', encoding = 'utf-8') as f:
        article = f.read()
        f.close()
        m = re.sub(u'динозавр?', u'кот', article)
        m = re.sub(u'Динозавр?', u'Кот', m)
        n = re.sub(u'<.*?>', u'', m, flags = re.U)
        print(n)
        f = open('text.txt', 'w',encoding = 'utf-8')
        f.write(n)
        f.close
replace()

        
