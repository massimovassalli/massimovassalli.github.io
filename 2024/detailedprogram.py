import csv

f = open('2024/fullprogram.tpl','r')
html = f.read()
f.close()

mycode = '<div class="row row-cols-1 row-cols-md-2">\n'

sessions={}
with open('2024/oral.csv', mode ='r') as f:
    csvFile = csv.reader(f)
    for elements in csvFile:
        session = elements[9]
        if session not in sessions and session!='Session':
            sessions[session]=[]
        if elements[8]=='A':
            sessions[session].append([elements[i] for i in [1,2,3,4,5,7,0]])

headers = ['3/3@17:00','4/3@9:00','4/3@16:00','5/3@9:00','5/3@14:00','6/3@9:00','6/3@16:00','7/3@9:00']
titles = ['Opening session','Nanomechanics and Mechanosensing','Cellular mechanobiology and mechanotransduction','Modelling mechanobiology',
          'Round Table Discussion','Collective cellular processes','Organoids and multicellular systems','Closing session']

order=['Opening','Nanomechanics and Mechanosensing','Cellular Mechanobiology and Mechanotransduction',
       'Modelling mechanobiology','Discussion','Collective Cellular Processes','Organoids and Multicellular Systems','Closing']
headses={}
i=0
for ses in order:
    headses[ses]=headers[i]
    i+=1
titses={}
i=0
for ses in order:
    titses[ses]=titles[i]
    i+=1

invited = 45
contributed = 25
sponsor = 15
coffee = 30

for ses in order:
    min=0
    data = sessions[ses]
    card = '''<div>\n'''
    card+='<h1>'+headses[ses]+'</h1>\n'    
    card+=f'<h2>{titses[ses]}</h2>\n'    
    card+='<ul>'
    for line in data:
        bold='font-weight: normal'
        if line[5]=='Y':
            bold='font-weight: bold'
            min+=invited
        else:
            if line[6]=='c':
                min+=coffee
            elif line[6]=='s':
                min+=sponsor
            else:
                min+=contributed
        name = f'{line[1]} {line[0]}'
        card+=f'<li><span style="{bold}">{name} [{line[2]}]</span> {line[3]}</li>'
    card+=f'</ul><span style="color:red;font-weight:bold;">{min}</span></div>'
    mycode+=card

f = open('2024/fullprogram.html','w')
f.write(html.replace('{XXX}',mycode))
f.close()
