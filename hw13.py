import os
from os.path import  isfile
def search():
    folder = 'C:/Users/Тимур/AppData/Local/Programs/Python/Python35-32'
    k = 0
    print(os.listdir(folder))
    for f in os.listdir(folder):
             if  not isfile(f):
                 if '_'  in f:
                     k = k + 1
                     print('file: ', f)
                 if ' ' in f:
                     k = k + 1
                     print('file: ', f)    
    print(k)
search()
