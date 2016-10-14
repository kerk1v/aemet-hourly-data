#!/usr/bin/python
# encoding: utf-8
import StringIO
import sys
import csv
import urllib2
import string
import re
from geopy.geocoders import Nominatim

manylines = 1

with open('station.id') as stnfile:
    stations = csv.reader(stnfile, delimiter=';')
    for station in stations:
        stationProv = station[0]
        stationId = station[1]
        stationLoc = station[2]
        # Start of Geostuff
        geolocator = Nominatim()
        location = geolocator.geocode(stationLoc)
        try:
            lat = float(location.latitude)
            lon = float(location.longitude)
            geo = str(lat) + ',' + str(lon)
            print stationProv + ';' + stationId + ';' + stationLoc + ';' + geo
            # print finalLine
        except:
            finalLine = stationProv + ';' + stationId + ';' + stationLoc + ';******************** GEODATOS NO DISPONIBLES *********************'
            print finalLine
