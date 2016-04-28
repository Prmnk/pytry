import pyodbc
filename = 'abc23.txt'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=PRAMANIK-PC\SQLEXPRESS;DATABASE=AdventureWorks2012;trusted_connection=tcon')
cursor = cnxn.cursor()

cursor.execute("SELECT EmployeeManager.BusinessEntityID, EmployeeManager.ManagerID from EmployeeManager")
for row in cursor.fetchall():
    #print str(row[0]),',',row[1],',',str(row[2])
    saveFile=open(filename,'a') 
    lis = [str(row[0]),str(row[1])]
    lineToWrite = ','.join(lis) +'\n'
    saveFile.write(lineToWrite)
    
saveFile.close()

    