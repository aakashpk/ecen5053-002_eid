# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:42:10 2017

@author: Aakash
"""

import databaseOps
import datetime 

import matplotlib.pyplot as plt
import mpld3

#ts=([1,2,3,4],[10,25,34,23])
#plt.plot(ts)

full=databaseOps.db.all()

x=[x['temperature'] for x in full]

y=[databaseOps.getDateTime(y) for y in full]

#print(y)

#a=plt.plot(y,x)

#print(b)
import datetime
import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py
import plotly.tools as tls

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

x = np.array([datetime.datetime(2014, i, 9) for i in range(1,13)])
y = np.random.randint(100, size=x.shape)

plt.plot(x,y)
plt.tight_layout()

fig = plt.gcf()
plotly_fig = tls.mpl_to_plotly( fig )

print(plotly_fig)

#py.iplot(plotly_fig, filename='mpl-time-series')
#div = notebook_div(plot)
#databaseOps.showdb()
#h,t = databaseOps.getData()
#a,b = databaseOps.calcDayMaximum("temperature")
#print(databaseOps.getDateTime(databaseOps.db.all()[-1]))



#print(databaseOps.db.all())