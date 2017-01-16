def name(title):
    with open (title+'.txt', 'r', encoding ='utf-8') as f:
        text=f.read()
        words=text.split(' ')
    return words
def ous():
    words = name("title") 
    p = 0
    k = 0
    for i, word in enumerate (words):
        if words[i].count("ous"):
            p = p + len(words[i])
            k = k + 1
    print(p / k)
ous()
