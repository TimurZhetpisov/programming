a = []
while True:
   word = input('Add a word')
   if word ==('') :break
   elif word.endswith ('tur'):
      a.append(word)
print ('\n'. join(a))
