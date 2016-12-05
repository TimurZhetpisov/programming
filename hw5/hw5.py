f = open('C:\\Users\\Тимур\\Desktop\\text.txt', 'r')
k = 0
l = [line.strip() for line in f]
p = str (l)
x=p.count(" ")
x=x+1
p=p.split()
for elem in p:
        if len(elem) > 10:
            k += 1
percent = k / x * 100
print(percent)



 
