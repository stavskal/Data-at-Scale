from mpl_toolkits.basemap import Basemap
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import OrderedDict
from datetime import time
import seaborn as sns

from numpy import sum as suma



colorMapping = {}
dayMapping = {}
sf = pd.read_csv('sanfrancisco_incidents_summer_2014.csv')
sf1 = sf.where(sf['PdDistrict']=='Central')
times = sf['Time'].values

uniCrimes = sf['Category'].unique()
print(len(uniCrimes))

crimesDay={}
crimesNight={}
crimesTotal={}

j=0
night1 = time(21,0)
night2 = time(9,0)
timeOfDay=[]
month={'8':'August','7':'July','6':'June'}
monthList=[]
for i in zip(sf['Time'],sf['Category'],sf['Date']):
	monthList.append(month[i[2][1:2]])
	curTime = time(int(i[0][0:2]),int(i[0][3:5]))

	if curTime<night1 and curTime>night2:

		timeOfDay.append('Day')
		print(i[1])
		if i[1] not in crimesDay.keys():
			crimesDay[i[1]] = 0
		else:
			crimesDay[i[1]] += 1
	else:
		timeOfDay.append('Night')
		print(i[1])
		if i[1] not in crimesNight.keys():
			crimesNight[i[1]] = 0
		else:
			crimesNight[i[1]] += 1
	if i[1] not in crimesTotal.keys():
		crimesTotal[i[1]] = 0
	else:
		crimesTotal[i[1]] += 1

crimeCountD=[]
crimeCountN=[]
crimeCount=[]
for i in sf['Category']:

	if i in crimesDay.keys():
		crimeCountD.append(crimesDay[i])
	else:
		crimeCountD.append(0)

	if i in crimesNight.keys():
		crimeCountN.append(crimesNight[i])
	else:
		crimeCountN.append(0)

	if i in crimesTotal.keys():
		crimeCount.append(crimesTotal[i])
	else:
		crimeCount.append(0)

sf['Month'] = pd.Series(np.array(monthList), index=sf.index)
sf['timeOfDay'] = pd.Series(np.array(timeOfDay), index=sf.index)
sf['testSum'] = pd.Series(np.ones(len(crimeCount)), index=sf.index)
sf['CrimeCount'] = pd.Series(np.array(crimeCount), index=sf.index)
sf['CrimeCountD'] = pd.Series(np.array(crimeCountD), index=sf.index)
sf['CrimeCountN'] = pd.Series(np.array(crimeCountN), index=sf.index)

print(sf.head())
topcrimes = OrderedDict(sorted(crimesDay.items(),reverse=True,key=lambda t: t[1]))
print('--------------------------------')

print(topcrimes)

#crimesDay = {'Monday': 1232, 'Tuesday': 1236,  'Wednesday': 1227, 'Thursday': 1234, 'Friday': 1444, 'Saturday': 1582,'Sunday': 1504}
#crimesOrd = 


sf.Category = sf.Category.replace()
#print(crimesDay.keys())
#ax = sns.barplot(x='testSum',y='Category',hue='PdDistrict',data=sf, estimator=suma)
#ax = sns.pairplot(sf,hue='Month',palette='husl')
sf1 = sf[(sf['Category']=='LARCENY/THEFT') | (sf['Category']=='OTHER OFFENSES') | (sf['Category']=='NON-CRIMINAL')| (sf['Category']=='ASSAULT')| (sf['Category']=='VEHICLE THEFT')]
ax = sns.barplot(x='testSum',y='PdDistrict',data=sf1, estimator=suma)
#ax.savefig('crimesdisttest.png')
#ax.set_xticks(x)
#ax.set_xticks(range(0,len(x)),rotation=45)
plt.title('At which districts 5 most popular crimes are commited')
#plt.ylabel('Number of crimesDay')
plt.xlabel('Number of indicents')
fig = ax.get_figure()
fig.set_size_inches(12,8)
fig.savefig('crimesdisttest.png')
#lon ,lat = map1(listlon,listlat)

#map1.plot(lon, lat, 'bo' ,markersize=3)
#plt.savefig('testmap1.png')


	#map1.plot(lon,lat,  , markersize=2)"""