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
                    with open('newcountry.json','r') as ff:
                        data1=json.load(ff)
                    if city in data1:
                        print (city)
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
                    print (city)
                    if count %10 == 0:
                        print (count)
                    readed = json.load(open('newcountry.json','r'))
                    readed[city] = ((location.latitude,location.longitude))
                    json.dump(readed,open('newcountry.json','w'))
                    if count%50 == 0 :
                        time.sleep(1)
    except Exception:
        print ('error')
        time.sleep(5)
        continue
