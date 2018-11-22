
# Reading an excel file using Python 
import xlrd 
import json
#import string
#import codecs
#from io import open
# Give the location of the file 
loc = ("C:\\Users\\saiful.bhuiya\\Desktop\\PythonTest\\Generali Language File_DE_FR.xlsx") 
#loc = ("C:\Users\\saiful.bhuiya\\Desktop\\PythonTest\\Test.xlsx")  

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
data = {}  
for i in range (1,245):
        data[sheet.cell_value(i ,1)] = []
# For row 0 and column 0 
#for i in range(1,4):
#    for j in range(1,3):
#        print(sheet.cell_value(i ,j))

for i in range (1, 245 ):
        #print(sheet.cell_value(i ,3))                         
        data[sheet.cell_value(i ,1).encode("utf-8")].append({
                'en' : sheet.cell_value(i ,2).encode("utf-8"),
                'de' : sheet.cell_value(i ,3).encode("utf-8"),
                'fr' : sheet.cell_value(i ,4).encode("utf-8")
        })


 

with open('data1.json', 'w') as outfile:  
    json.dump(data, outfile,ensure_ascii=False,sort_keys=False)    