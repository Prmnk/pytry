import csv
f = open('C:\Users\pramanik\Downloads\data.csv')
csv_f= csv.reader(f)

file = 'abc.txt'

for row in csv_f :
    for i in range(0,len(row)):
       row[i]=row[i].replace(',','')
    ','.join(row)
    saveFile=open(file,'a') 
    lineToWrite = ','.join(row)+'\n'
    saveFile.write(lineToWrite)
    
saveFile.close()