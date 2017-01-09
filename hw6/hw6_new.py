import random
def noun():
    file = open('noun.txt', 'r', encoding = 'utf8')
    f = file.read()
    nouns = f.split('\n')
    return random.choice(nouns)

def conjunction():
    file = open('conjunction.txt', 'r', encoding = 'utf8')
    f = file.read()
    conjunctions = f.split('\n')
    return ", "+random.choice(conjunctions)

def adjective():
    file = open('adjective.txt', 'r', encoding = 'utf8')
    f = file.read()
    adjectives = f.split('\n')
    return random.choice(adjectives)
 
def verb():
    file = open('verb.txt', 'r', encoding = 'utf8')
    f = file.read()
    verbs = f.split('\n')
    return random.choice(verbs)

def place():
    file = open('place.txt', 'r', encoding = 'utf8')
    f = file.read()
    places = f.split('\n')
    return random.choice(places)
 
def part_SS():
  return adjective()+" " +noun()+" " +verb()+" "+place()
 
def SS():
  return (part_SS()+conjunction()+" "+part_SS()+".").capitalize()
 
def IfSP():
  return "в то время как " + adjective()+" " + noun() +" "+ verb() +" "+ place() + ", " + noun()+" "+verb()
 
def TimeSP():
  return "когда " + noun() +" "+ verb() + ", "+ adjective()+" "+ noun()+" "+verb()
 
 
def SP():
  ver = random.randint(1,2)
  if (ver == 1):
    return (IfSP()+".").capitalize()
  else:
    return (TimeSP()+".").capitalize()

print("УДИВИТЕЛЬНЫЙ ШЕДЕВР НАПИСАННЫЙ МАШИНОЙ") 
for i in range(random.randint(5,10)):
  sen = random.randint(1,2)
  if(sen==1):
    print(SS())
  else:
    print(SP())
print("НУ ВОТ И ВСЕ, РЕБЯТА")

