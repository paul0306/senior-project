import distance as d
import demoSVR as s
import demoXGBoost as x

def getPrice(latA, longA, country, houseType, internal):
    external = d.findDist(latA, longA, country)
    factor = [internal + external]
    fileName = country + houseType
    if (fileName == '桃園透天' or fileName == '台南大樓' or fileName == '台南透天' or fileName == '高雄大樓'):
        return s.pred(country, houseType, factor)
    else:
        return x.pred(country, houseType, factor)