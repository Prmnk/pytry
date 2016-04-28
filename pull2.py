import urllib2
import time
import datetime

stocksToPull = 'AAPL','TSLA'

def pullData(stock):
    try:
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%y-%m-%d %H:%M:%S'))
        urlToVisit='http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
        saveFileLine = stock+'.txt'
        
        try:
            readExistingData = open(saveFileLine, 'r').read()
            splitExisting = readExisitngData.split('\n')
            mostRecentLine = splitExisting[-2]
            lastUnix = mostRecentLine.split(',')[0]
        except :
            lastUnix = 0
            
        saveFile = open(SaveFileLine,'a')
        sourceCode = urllib2.urlopen(urlToVisit)
        splitSource = sourceCode.split('\n')
        for eachLine in splitSource:
            if 'values' not in eachLine:
                splitLine = eachLine.split(',')
                if len(splitLine)==6:
                     if int(splitLine[0]) > int(lastUnix):
                         lineToWrite = eachLine +'\n'
                         saveFile.write(lineToWrite) 
        saveFile.Close() 
                    
    except:
        print 'e'
        