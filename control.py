#!/usr/bin/python3
import distance as d
import demoSVR as s
import demoXGBoost as x

def getPrice(latA, longA, country, houseType, internal):
    external = d.findDist(latA, longA, country)
    factor = [internal + external]
    fileName = country + houseType
    if (fileName == 'tynHouse' or fileName == 'tnnApart' or fileName == 'tnnHouse' or fileName == 'khhApart'):
        return s.pred(country, houseType, factor)
    else:
        return x.pred(country, houseType, factor)