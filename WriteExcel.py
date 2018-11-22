
# import xlsxwriter module 
import xlsxwriter 
import xlrd 
import json

# this workbook is the file where the excel file will be written  
workbook = xlsxwriter.Workbook('AllTranslationData.xlsx') 
# this is the location from where a excel file data will be read
loc = ("C:\\Users\\saiful.bhuiya\\Desktop\\PythonTest\\Generali Language File_DE_FR.xlsx")

#this is the worksheet of the write excel file
worksheet = workbook.add_worksheet("My sheet") 

# this is the worksheet of the read excel file
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  

# a list created to store the language data
data = ()

# the data read form the previous excel file uploaded to the list

for i in range(245):
    data = data+ ([sheet.cell_value(i ,1),sheet.cell_value(i ,2),sheet.cell_value(i ,3),sheet.cell_value(i ,4)],)

#print(data)

#opening the untranslated json file

with open('C:\\Users\\saiful.bhuiya\\Desktop\\PythonTest\\other.json', 'r') as f:
    otherfile = json.load(f)


for i,j in otherfile.items():
    #print(i)
    #print(otherfile[i]['en'])
    data = data +([i,otherfile[i]['en'],"",""],)

#for i in range(len(otherfile)):


 
  
  
# Start from the first cell. Rows and 
# columns are zero indexed. 
row = 0
col = 0
  
# Iterate over the data and write it out row by row. 
for key, en,de,fr in (data): 
    worksheet.write(row, col, key) 
    worksheet.write(row, col + 1, en)
    worksheet.write(row, col + 2, de)
    worksheet.write(row, col + 3, fr) 
    row += 1
  
workbook.close() 