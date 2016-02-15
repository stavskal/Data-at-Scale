from mpl_toolkits.basemap import Basemap
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import OrderedDict
from datetime import time
import seaborn as sns
from matplotlib import colors
import six

from numpy import sum as suma

plt.title('Crime incidents in Southern district throughout the day')
plt.ylabel('Number of incidents')
plt.xlabel('Hour of day')

colorMapping = {}
dayMapping = {}
sf = pd.read_csv('sanfrancisco_incidents_summer_2014.csv', parse_dates={"Datetime": [5]})
sf = sf.set_index(['Datetime'])

distr_list = pd.unique(sf.Category.ravel())
print(distr_list)
sf = sf.dropna()
i=0
#colors =['blue','green','red','cyan','magenta','yellow','black','white','purple','orange']
colors = list(six.iteritems(colors.cnames))
for dist in distr_list:
	sf1 = sf.where(sf['Category']==dist)
	#Data is kinda ready after that
	#sf1 = sf1.where(sf['Category']=='LARCENY/THEFT')

	#print(sf1.head(20))
	print('-----------------------------------------------------')
	#print(sf1.head(5))
	#sf1 = sf1.groupby(['DayOfWeek'])
	grouped = sf1.groupby(pd.TimeGrouper(freq='60Min')).count()
	grouped['index1'] = grouped.index.hour
	pdnum = grouped.as_matrix(['index1','Resolution'])
	time = pdnum[:,0]
	values = pdnum[:,1]
	ax = sns.tsplot(data=values, time=time,legend=True, color=colors[i], condition=dist)
	i+=1
plt.legend(bbox_to_anchor=(1.01,1),loc=2,borderaxespad=0)
fig = ax.get_figure()
fig.set_size_inches(13,8)
fig.savefig('crimes_hour_all.png')
#time = np.array(grouped.idx)
#values = np.array(grouped['Resolution'])

print(time,values)


print(grouped.head(27))


#