#!/usr/bin/python
# encoding: utf-8
import StringIO
import sys
import csv
import urllib2
import string

manylines=1

if len(sys.argv)==2:
    manylines=int(sys.argv[1])

if len(sys.argv)>2:
    print "Usage: ./aemet-get.py [number of last values to retrieve]"
    sys.exit(254)

if manylines > 24:
    print "The maximum of last values that can be retrieved from AEMET is 24"
    sys.exit(254)

with open('/home/volkerk/aemet-hourly-data/station.id') as stnfile:
    stations = csv.reader(stnfile, delimiter=';')
    for station in stations:
        stationProv = station[0]
        stationId = station[1]
        stationLoc = station[2]
        # we construct the curl URI
        curlUri='http://www.aemet.es/es/eltiempo/observacion/ultimosdatos_' + stationId + '_datos-horarios.csv?k=and&l=' + stationId + '&datos=det&w=0&f=temperatura&x=h24'
        urlResponse = urllib2.urlopen(curlUri)
        aemetData = urlResponse.read()
        lastline = manylines+4
        for thisline in range (4,lastline,1):
            aemetDataLast = aemetData.splitlines()[thisline]
            lineOut = '"' + stationProv + '","' + stationId + '","' + stationLoc + '",' + aemetDataLast
            # now let's separate into csv, we need this to build the unique ID for ElasticSearch
            dataLine = StringIO.StringIO(lineOut)
            csvData = csv.reader(dataLine, delimiter=',')
            for csvDataLine in csvData: 
                rawId = csvDataLine[3] + csvDataLine[1]
		id=filter(str.isalnum, rawId)
            #and now for constructing our CSV output and printing it, first field is ID
            outLine = '"' + id + '",' + lineOut
            print outLine
