#!/usr/bin/python
# encoding: utf-8
import csv
import urllib2

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
        aemetDataLast = aemetData.splitlines()[4]
        lineOut = '"' + stationProv + '";' + '"' + stationId + '";' + '"' + stationLoc + '";' + aemetDataLast
        print lineOut
        
