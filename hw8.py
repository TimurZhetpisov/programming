import random
d = {'Алые': 'Паруса',
     'Пластмассовый': 'Мир',
     'Белые': 'Розы',
     'Синее': 'Море',
     'Черный': 'Передел'}
key_list = []
for key in d:
        key_list.append(key)
print("Подсказка: ")
k = random.randint(1,5)
print(d[key_list[k]])
count = 0
while(input() != key_list[k]):
    count+=1
    print("Попытка номер ",count)
    count = count + 1
print("Ура, вы выиграли!")
print(count)
