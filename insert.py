import pyodbc
import csv
f = open('abc.txt')
csv_f= csv.reader(f)

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=PRAMANIK-PC\SQLEXPRESS;DATABASE=AdventureWorks2012;trusted_connection=tcon')
cursor = cnxn.cursor()

insert='Insert into Test Values (?,?); Commit'
for row in csv_f:
    if row[1]!='Open':
        print row[0],int(float(row[1]))
        cursor.execute(insert,(row[0],int(float(row[1]))))

cursor.close()
del cursor
cnxn.close()