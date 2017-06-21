from geopy.geocoders import Nominatim
import re
import time
geolocator = Nominatim()
f = open('data.txt',encoding='utf-8')
source=f.read()
f.close()
a=[]
a = source.split('}}}')
i1=0
count=0
while i1<len(a):
    b=[]
    b=a[i1].split(',')
    i1=i1+1
    i2=1    
    while i2<len(b):
        count=count+1
        if count%10==0:
            print(count)
        c=[]
        c=b[i2].split('"')
        if c[1]=='':
            i2=i2+1
            continue
        try:
            location = geolocator.geocode(c[1])
        except Exception:
            print(c[1])
            print('error')
            time.sleep(5)
            i2=i2+1
            continue
        if location == None:
            print(c[1])
            print('cannot find position')
            i2=i2+1
            continue
        f2 = open('test.txt','r+')
        f2.read()
        f2.write(c[1])
        f2.write('\t')
        f2.write(str(location.latitude))
        f2.write('\t')
        f2.write(str(location.longitude))
        f2.write('\n')
        f2.close()
        i2=i2+1
        time.sleep(1)
#b1的c1是国家，b2到bn的c1是城市