import re
def search():
    with open('F.xml', 'r', encoding = 'utf - 8') as f:
        k = 5
        for line in f:
            if '</teiHeader>' in line:
                break
            elif '</teiHeader>' not in line:
                k = k + 1
            print(k)
        f.close()
        f = open('number.txt', 'w',encoding = 'utf-8')
        k = str(k)
        f.write(k)
        f.close()
search()
def dictn():
    d={}
    with open('F.xml', 'r', encoding = 'utf - 8') as f:
        for line in f:
             n = re.findall('type="*"', f)
             d = {n}
             if(key in d):
                 d[key] = d[key]+1
             else:
                 d[key]=1
                 print(d)
dictn()
                 



        
             
            
        
