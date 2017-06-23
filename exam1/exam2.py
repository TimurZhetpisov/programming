import re
import os
import csv
def open_file_tree():
    names = {}
    file_tree = os.walk('news')
    for root, dirs, files in os.walk('news'):
        for f in files:
            with open(os.path.join(root,f), 'r') as p:
                texts = p.readlines()
                se_num = 0
                for text in texts:
                    if '/se' in text:
                        se_num = se_num + 1
            names[f] = se_num
    create_txt(names)
def create_txt(dict):
    new = ""
    with open("result.txt", "w", encoding="utf-8") as file:
        for i in dict.keys():
            new += "\n" + i.strip() + "\t" + str(dict[i])
        file.write(new)    

def create_table():
    data1 = u"FILENAME" + 'AUTHOR' + 'DATE'
    with open('result2.csv', 'w') as file:
        file.write(data1)

def change_table(file,auth,date):
    data = "\n" + file + auth  + date
    with open('result2.csv', 'a') as file:
        file.write(data)
        
def table():
    date = ''
    author = ''
    create_table()
    for root, dirs, files in os.walk('news'):
        for f in files:
            with open(os.path.join(root, f), 'r') as p:
                oneline = p.read()
                for i in re.finditer(r"<meta content=\"(.*?)\" name=\"author\"></meta>", oneline):
                    author = i.group(1)
                for j in re.finditer(r"<meta content=\"(.*?)\" name=\"created\"></meta>", oneline):
                    date = j.group(1)
        change_table(f, author, date)
open_file_tree()
table()
    
