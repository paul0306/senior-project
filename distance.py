import math as m
import pandas as pd

def calDist(latA,longA,latB,longB):
    return ((6371*m.acos(m.cos(m.radians(latA))*m.cos(m.radians(latB))*m.cos(m.radians(longB)-m.radians(longA))+m.sin(m.radians(latA))*m.sin(m.radians(latB)))))

def findDist(latA, longA, country):
    df = pd.read_excel("./environ/" + country + ".xlsx")
    distList = []
    tcExternal = ['公園','火車站','美術館','音樂廳','國民運動中心','捷運','博物館','醫院','圖書館','賣場','國小','國中','轉運站',
                 '工業區','汙水處理廠','垃圾場','發電廠','墓地','機場','殯儀館','高鐵','高速/快速公路']
    tnExternal = ['公園','火車站','美術館','音樂廳','國民運動中心','博物館','醫院','圖書館','賣場','國小','國中','轉運站',
                 '工業區','汙水處理廠','垃圾場','發電廠','墓地','殯儀館','機場','高速/快速公路','高鐵']
    otherExternal = ['公園','火車站','美術館','音樂廳','國民運動中心','捷運','博物館','醫院','圖書館','賣場','國小','國中','轉運站',
                    '工業區','汙水處理廠','垃圾場','發電廠','墓地','殯儀館','機場','高速/快速公路','高鐵']
    if (country == 'tnn'):
        model = tnExternal
    elif (country == 'txg'):
        model = tcExternal
    else :
        model = otherExternal
    for i in range(len(model)):
        data = []
        latB = df[model[i]+'緯度'].values.tolist()
        longB = df[model[i]+'經度'].values.tolist()
        for j in range(len(latB)):
            data.append(calDist(latA, longA, latB[j], longB[j]))
        distList.append(min(data))
    return distList