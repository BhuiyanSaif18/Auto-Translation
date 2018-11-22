import json

data = {}  
data['people1'] = [] 
data['people2'] = [] 
data['people3'] = []  


with open('data1.json', 'w') as outfile:  
    json.dump(data, outfile)