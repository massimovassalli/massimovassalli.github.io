import csv

f = open('2024/program.tpl','r')
html = f.read()
f.close()

mycode = '<div class="row row-cols-1 row-cols-md-2">\n'

sessions={}
with open('2024/database.csv', mode ='r') as f:
    csvFile = csv.reader(f)
    for elements in csvFile:
        session = elements[9]
        if session not in sessions and session!='Session':
            sessions[session]=[]
        if elements[8]=='A':
            sessions[session].append([elements[i] for i in [1,2,3,4,5,7]])

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
colses={}
i=0
colors=['info','primary','primary','primary','info','primary','primary','info']
for ses in order:
    colses[ses]=colors[i]
    i+=1

embo='<img src="./assets/EMBO-logo.png" width="100">'

for ses in order:
    data = sessions[ses]
    card = '''<div class="col mb-4">
    <div class="card mb-3">\n'''
    card+='<div class="card-header">'+headses[ses]+'</div>\n'    
    card+='<div class="card-body">\n'
    card+=f'<h5 class="card-title text-{colses[ses]}">{titses[ses]}</h5>\n'    
    card+='''
    <!-- <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>-->
  </div>
  <ul class="list-group list-group-flush">
  '''
    for line in data:
        if line[3]=='w':
            over='<span class="text-warning"></span>'
        else:
            over=f'<button data-bs-toggle="popover" data-bs-placement="top" data-bs-content="{line[4]}" role="button" data-bs-trigger="focus" data-bs-title="{line[3]}" class="btn btn-link text-decoration-none text-warning">{line[3]}</button>'
        bold=''
        if line[5]=='N':
            bold=f'text-{colses[ses]}'
        name = f'{line[1]} {line[0]}'
        if line[0]=='Treutlein' or line[0]=='Ruprecht':
            line[2]+=embo
        card+=f'<li class="list-group-item"><span class="{bold}">{name}</span>, '

        card+=f'<span class="text-secondary">{line[2]}</span><br>{over}</li>\n'
    card+='''</ul>
</div>
  </div>\n'''
    mycode+=card

mycode+='</div>'


f = open('2024/program.html','w')
f.write(html.replace('{XXX}',mycode))
f.close()
