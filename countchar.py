import csv
from datetime import date, timedelta
import re
import os.path
import sys
import zipfile

filename = 'readme.docx'
data_filename = 'data.csv'

# extract total characters from docx
re_tag = re.compile("\<.+?\>")
with zipfile.ZipFile(filename, 'r') as z:
    #print(z.namelist())
    d = z.read('word/document.xml').decode("utf8")
d = re_tag.subn("",d)

# initialize values
current_status = str(date.today())+','+str(len(d[0]))
content = []

# read csv file and construct new content
if os.path.exists(data_filename):
    with open(data_filename, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        isOverwritten = False
        for row in csvreader:
            if row[0] == str(date.today()):
                content += [current_status]
                isOverwritten = True
                break
            else:
                content += [','.join(row)]
        if not isOverwritten:
            content += [current_status]
    
# initialize csv file if needed
if len(content) <= 2: # if !os.path.exists(data_filename), this is True
    content = ["date,chars",str(date.today()-timedelta(1))+",0",current_status]
    print(data_filename + " is initialized")

# rewrite csv file        
with open(data_filename, "w", newline='') as csvfile:
    csvfile.write('\n'.join(content))
