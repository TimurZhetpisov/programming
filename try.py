from flask import Flask
from flask import url_for, render_template, request, redirect
import json
import re
import sqlite3
land = {}
age = {}
sex = {}
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('q.html')
@app.route('/now')
def main():
    data = dict(request.args)
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists Form(Age integer, Land text, Sex text, Language text, Pulover text, Marketing text, Boyfriend text)''')
    c.execute("INSERT INTO Form (Age, Land, Sex, Language, Pulover, Marketing, Boyfriend) VALUES(?,?,?,?,?,?,?)",
    [data['возраст'][0], data['страна'][0], data['пол'][0], data['язык'][0], data['пуловер'][0],data['маркетинг'][0], data['бойфрэнд'][0]])
    conn.commit()
    with open('results_data.json', "a", newline="") as file: 
        file.write(json.dumps(data, ensure_ascii = False))
    language = request.args['язык']
    land = request.args['страна']
    s = request.args['пол']
    if s not in sexs:
        sex[s] = '1'
    else:
        sex[s] = str(int(sex[s]) + 1)
    if language not in lang:
        lang[language] = '1'
    else:
        lang[language] = str(int(lang[language]) + 1)
    if land not in lands:
        lands[land] = '1'
    else:
        lands[land] = str(int(lands[land]) + 1)
    pall = []
    lall = []
    sall = []
    for i in sexs:
        s = [i, int(sexs[i])]
        sall.append(s)
    for i in lands:
        p = [i, int(lands[i])]
        pall.append(p)
    for i in lang:
        l = [i, int(lang[i])]
        lall.append(l)
    with open('languages.json', "w", newline="") as file:
        file.write(json.dumps(lall, ensure_ascii = False))
    with open('lands.json', "w", newline="") as file:
        file.write(json.dumps(pall, ensure_ascii = False))
    with open('sex.json', "w", newline="") as file:
        file.write(json.dumps(sall, ensure_ascii = False))
@app.route('/statistics')
def stat():
       with open('lands.json', "r") as file: 
        pchstring = file.read()
        pchstring = re.sub(r'",', ':', pchstring)
        pchstring = re.sub(r'\[', '', pchstring)
        pchstring = re.sub(r']', '', pchstring)
        pchstring = re.sub(r'"', '', pchstring)
        lands = pchstring.split(',')
        with open('sexs.json', "r") as file: 
            sexs = file.read()
            sexs = re.sub(r'",', ':', sexs)
            sexs = re.sub(r'\[', '', sexs)
            sexs = re.sub(r']', '', sexs)
            sexs = re.sub(r'"', '', sexs)
            sex = sexs.split(',')
            with open('languages.json', "r") as file: 
                lchstring = file.read()
                lchstring = re.sub(r'",', ':', lchstring)
                lchstring = re.sub(r'\[', '', lchstring)
                lchstring = re.sub(r']', '', lchstring)
                lchstring = re.sub(r'"', '', lchstring)
                languages = lchstring.split(',')
                return render_template('statistics.html', languages = languages, lands = lands, sexs = sex)
@app.route('/json')
def complete():
    with open('results_data.json', "r") as file: 
        content = file.read() 
    return render_template('jsn.html', content = content)
@app.route('/search')
def search():
    return render_template('search.html')
@app.route('/results')
def results():
    final = []
    forms2 = []
    searched = request.args['search']
    with open('results_data.json', "r") as file: 
        content = file.read()
    forms = content.split('}')
    for i in forms:
        j = re.sub(r'(\[|]|"|{)', '', i)
        forms2.append(j)
    for j in forms2:
        if re.search(searched, j):
            final.append(j)
    return render_template('results.html', final = final) 
if __name__ == '__main__':
    app.run(debug=True)
