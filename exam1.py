import re
import os
import csv
def open_file_tree():
    names = {}
    file_tree = os.walk('news')
    for root, dirs, files in os.walk('news'):
        for f in files:
            with open(os.path.join(root,f), 'r') as f0:
                texts = f0.readlines()
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
open_file_tree()

    
