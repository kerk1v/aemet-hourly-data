#!/usr/bin/python
# encoding: utf-8
import sys
import csv
import urllib2

manylines=int(sys.argv[1])
if manylines > 24:
    print "The maximum of last values that can be retrieved from AEMET is 24"
    sys.exit(254)

with open('station.id') as stnfile:
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
            lineOut = '"' + stationProv + '",' + '"' + stationId + '",' + '"' + stationLoc + '",' + aemetDataLast
            print lineOut
        
