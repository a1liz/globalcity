from geopy.geocoders import Nominatim
import json
import time
geolocator = Nominatim()

with open('countriesToCities.json', 'r') as f:
    data = json.load(f)

count = 0
i = 0
while i != 10 :
    try :
        i+=1
        for key in data :
            for city in data[key] :
                if key == u'China' :
                    if city == u"" :
                        continue
                    with open('newcountry.json','r') as ff:
                        data1=json.load(ff)
                    if city in data1:
                        continue
                    try :
                        citystring = city.encode()
                    except UnicodeEncodeError:
                        readed = json.load(open('errorcountry.json','r'))
                        readed[city] = city
                        json.dump(readed,open('errorcountry.json','w'))
                        continue
                    location = geolocator.geocode(citystring)
                    if location == None:
                        continue
                    count += 1
                    print city
                    if count %10 == 0:
                        print count
                        time.sleep(3)
                    readed = json.load(open('newcountry.json','r'))
                    readed[city] = ((location.latitude,location.longitude))
                    json.dump(readed,open('newcountry.json','w'))
                    if count%50 == 0 :
                        time.sleep(5)
    except Exception,e:
        print str(e)
        time.sleep(5)
        continue
