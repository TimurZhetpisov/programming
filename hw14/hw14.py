import os
from os.path import  isfile
def search():
    folder = 'C:/Users/Тимур/AppData/Local/Programs/Python/Python35-32'
    p = 0
    names = ['test']
    print(os.listdir(folder))
    for files in os.walk(folder):
        for f in files:
            for i in range(p):
                if name[i] != (f.split('.')[0]):
                    names.append(f.split('.')[0])
                    p += 1
    print(p)
    for name in names:
        print(name)
search()
                                                     
            
