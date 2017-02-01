import re
pattern = r'[с][ъ][е][^\s.]*'
with open('word.txt', encoding='UTF-8') as file:
    for row in file:
        find = re.findall(pattern, row)
        for i in (len(find)):
            print('Найденные элементы')
            print(elem[i])
