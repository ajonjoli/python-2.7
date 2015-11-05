from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

mp = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

mp.drawcoastlines()
mp.drawcountries()
#mp.drawstates()
#mp.drawrivers()
mp.fillcontinents(color='#aaffaa', lake_color='gray')
mp.drawmapboundary()
#mp.bluemarble()	#parece vista espacial, high definition needs
plt.title('Quick Base Map Geoplotting')

lat,lon=20.76,-100
x,y=mp(lon,lat)
mp.plot(x,y,'ro')

lat,lon=[20.7,-10],[100,-100]
x,y=mp(lon,lat)
mp.plot(x,y,'bo',markersize=10,alpha=0.5)

plt.show()
