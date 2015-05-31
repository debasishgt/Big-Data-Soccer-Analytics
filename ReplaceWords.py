import json

with open('jsonData.json') as json_file:
    data = json.load(json_file)

file = open('C:\\Data_Sector\\Student\\CSULA\\Quarter-Terms\\Q3-Spring2015\\CS594-BigData\\new-dashboard.html','r+')
contents = file.read()
contents = contents.replace('#FNAME#',data[0]['id'])
contents = contents.replace('#FDATA#',data[0]['value'])

contents = contents.replace('#SNAME#',data[1]['id'])
contents = contents.replace('#SDATA#',data[1]['value'])

contents = contents.replace('#TNAME#',data[2]['id'])
contents = contents.replace('#TDATA#',data[2]['value'])

contents = contents.replace('#FRNAME#',data[3]['id'])
contents = contents.replace('#FRDATA#',data[3]['value'])

contents = contents.replace('#FVNAME#',data[4]['id'])
contents = contents.replace('#FVDATA#',data[4]['value'])

contents = contents.replace('#SXNAME#',data[5]['id'])
contents = contents.replace('#SXDATA#',data[5]['value'])

with open('C:\\xampp\\htdocs\\webpy\\updated_dashboard.html','w') as new_dash:
    new_dash.write(contents)
