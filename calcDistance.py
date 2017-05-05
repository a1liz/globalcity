from math import *
def calcDistance(Lat_A, Lng_A, Lat_B, Lng_B):
    ra = 6378.140  # 赤道半径 (km)
    rb = 6356.755  # 极半径 (km)
    flatten = (ra - rb) / ra  # 地球扁率
    rad_lat_A = radians(Lat_A)
    rad_lng_A = radians(Lng_A)
    rad_lat_B = radians(Lat_B)
    rad_lng_B = radians(Lng_B)
    pA = atan(rb / ra * tan(rad_lat_A))
    pB = atan(rb / ra * tan(rad_lat_B))
    xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
    c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
    c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (xx + dr)
    return distance

import json

with open('newcountry.json','r') as f:
	data = json.load(f)
count=0
lon1=0
lat1=0
lon2=0
lat2=0
place1 = input()
place2 = input()
for key in data :
	if key== place1:
		lon1=data[key][0]
		lat1=data[key][1]
		count+=1
	if key==place2:
		lon2=data[key][0]
		lat2=data[key][1]
		count+=1
	if count==2:
		break
print(lon1)
print(lat1)
print(lon2)
print(lat2)
print(calcDistance(lon1, lat1, lon2, lat2))