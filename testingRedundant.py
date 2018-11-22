import json

#json = json.loads(open('C:\\Users\\saiful.bhuiya\\Desktop\\PythonTest\\untranslated.json').read())
#value = json['SELECT_GUARANTEE_TYPE']
#print(json['value'])


with open('C:\\Users\\saiful.bhuiya\\Desktop\\PythonTest\\untranslated.json', 'r') as f:
    untranslate = json.load(f)


with open('C:\\Users\\saiful.bhuiya\\Desktop\\PythonTest\\data1.json', 'r') as f:
    translate = json.load(f)


data = {}

#print(data)
# untranslated data 289
# translated data 243
# 69984
c = 0
d=0     
p =0
k = 0
i= 0      
for untrans in untranslate :
    
    for trans in translate:

        if untrans != trans:
            
            i = 1
        if untrans == trans:
            c = 1
        
    if c==0 and i ==1:
         k = k+1
         c=0
         i=0
        # print(untranslate[untrans])
         data[untrans] = untranslate[untrans]
         
    else:
        c=0
        i=0

        
print(data)

with open('other.json', 'w') as outfile:  
    json.dump(data, outfile,sort_keys=False)    