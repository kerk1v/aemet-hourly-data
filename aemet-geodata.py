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

with open('geo.id') as stnfile:
    stations = csv.reader(stnfile, delimiter=';')
    for station in stations:
        stationProv = station[0]
        stationId = station[1]
        stationLoc = station[2]
        geoId = station[3]
        # Start of Geostuff
        geoList = geoId.strip().split(",")
        geo1 = geoList[0]
        geo2 = geoList[1]
        geo = '"' + geo1[:7] + ',' + geo2[:8] + '"'
        print stationProv + ';' + stationId + ';' + stationLoc + ';' + geo
