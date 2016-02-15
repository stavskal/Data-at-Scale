from mpl_toolkits.basemap import Basemap
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as numpy
import pandas as pd
from datetime import time

colorMapping = {}
dayMapping = {}
sf = pd.read_csv('sanfrancisco_incidents_summer_2014.csv')


print(sf['Time'].head())
times = sf['Time'].values

uniCrimes = sf['Category'].unique()
cl=colors.cnames.keys()
for i in range(0,len(uniCrimes)):
	colorMapping[uniCrimes[i]] = cl[i]
print(colorMapping)

markers =['o','x','p','d','s','8','*']
uniDays = sf['DayOfWeek'].unique()
for i in range(0,len(uniDays)):
	dayMapping[uniDays[i]]=markers[i]


#print(sf[1:2])
listlon = list(sf['X'])
listlat = list(sf['Y'])




map1 = Basemap(projection='merc',resolution='f',area_thresh=0.1, 
	llcrnrlon=min(sf['X']),llcrnrlat=min(sf['Y']),
	urcrnrlon=max(sf['X']),urcrnrlat=max(sf['Y']))

map1.drawcoastlines()
map1.fillcontinents()
j=0
night1 = time(23,0)
night2 = time(5,0)
for i in zip(sf['X'],sf['Y'],sf['Category'],sf['DayOfWeek'],sf['Time'],sf['PdDistrict']):
	#print(i[0],i[1],i[2],i[3])
	curTime = time(int(i[4][0:2]),int(i[4][3:5]))
	#print(curDate)
#	if curTime<night1 or curTime>night2:
#		print(curTime)
	if i[5]=='SOUTHERN':
		lon, lat = map1(i[0],i[1])
		style = colorMapping[i[2]]
		mark = dayMapping[i[3]]
		map1.plot(lon,lat,color='b',marker='x',markersize=4)
	j+=1
	#print(j)
	if j==5000:
		break
#lon ,lat = map1(listlon,listlat)



#map1.plot(lon, lat, 'bo' ,markersize=3)
plt.title('Incidents that take place at Southern District')
plt.savefig('SOUTHERN.png')


	#map1.plot(lon,lat,  , markersize=2)"""