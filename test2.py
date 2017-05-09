from geopy.geocoders import Nominatim
import json
import time
geolocator = Nominatim()

with open('countriesToCities.json', 'r') as f:
    data = json.load(f)

count = 0
passcount = 0
i = 0
while i != 1 :
    try :
        i+=1
        for key in data :
            for city in data[key] :
                if key == u'China' :
                    if city == u"" :
                        print "have null city"
                        time.sleep(5)
                        continue
                    with open('newcountry.json','r') as ff:
                        data1=json.load(ff)
                    data1 = json.load(open('newcountry.json','r'))
                    data2 = json.load(open('errorcountry.json','r'))
                    data3 = json.load(open('passcountry.json','r'))
                    if city in data1:
                        continue
                    if city in data2:
                        continue
                    if city in data3:
                        continue
                    try :
                        citystring = city.encode()
                    except UnicodeEncodeError:
                        readed = json.load(open('errorcountry.json','r'))
                        readed[city] = city
                        json.dump(readed,open('errorcountry.json','w'))
                        continue
                    print citystring
                    location = geolocator.geocode(citystring)
                    if location == None:
                        passcount += 1
                        if passcount % 50 == 0 :
                            print passcount
                            time.sleep(5)
                        print "the location is null"
                        readed = json.load(open('passcountry.json','r'))
                        readed[city] = city
                        json.dump(readed,open('passcountry.json','w'))
                        continue
                    count += 1
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
