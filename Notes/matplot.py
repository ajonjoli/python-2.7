import matplotlib.pyplot as plt	#package: matplotlib, module: pyplot, alias: plot

#plt.title('MatPlotLib examplet')
#plt.xlabel('Eje X')
#plt.ylabel('Eje Y')

#plt.plot([1,2,3,4],[4,3,2,1])	#list args
#plt.plot((1,2,3,4),(5,4,3,2))	#tuple args


X=[]
Y=[]
#x=[1,2,3,4]
#y=[2,4,6,8]
leo=open('data.txt','r')
data=leo.read().split()
leo.close()

for PlotPair in data:
	xy=PlotPair.split(',')
	X.append(int(xy[0]))
	Y.append(float(xy[1]))

fig = plt.figure()	#canvas for customization
rect =fig.patch
rect.set_facecolor('#3131ff')	#background color

#plt.plot(X,Y)	#var args

ax1 = fig.add_subplot(2,2,1,axisbg='grey')	#graph color
#1,1,1= on a grid 1x1, use place 1; 2,2,4= on a grid 2x2, use place 4
ax1.plot(X,Y,'cyan',linewidth=3.3)	#line color and width

#ax1.tick_params(axis='x', color='cyan')
#ax1.tick_params(axis='y', color='red')
ax1.tick_params(axis='x', colors='cyan')	#grid lines color
ax1.tick_params(axis='y', colors='red')

ax1.spines['bottom'].set_color('white')	#margin color
ax1.spines['top'].set_color('white')
ax1.spines['left'].set_color('white')
ax1.spines['right'].set_color('white')

ax1.xaxis.label.set_color('cyan')	#labels color
ax1.yaxis.label.set_color('cyan')
ax1.yaxis.grid(True)

ax1.set_title('matplotlip ttl',color='white')
ax1.set_xlabel('Eje X')
ax1.set_ylabel('Eje Y')

ax2 = fig.add_subplot(222,axisbg='white')	#graph color
#ax2.plot(X,Y,'cyan',linewidth=3.3)	#line color and width
ax2.tick_params(axis='x', colors='black')	#grid lines color
ax2.tick_params(axis='y', colors='black')
ax2.spines['bottom'].set_color('black')	#margin color
ax2.spines['top'].set_color('black')
ax2.spines['left'].set_color('black')
ax2.spines['right'].set_color('black')
ax2.xaxis.label.set_color('black')	#labels color
ax2.yaxis.label.set_color('black')
ax2.xaxis.grid(True)	#grid lines
ax2.yaxis.grid(True)
ax2.set_title('matplotlip ttl',color='black')
ax2.set_xlabel('EjeX')
ax2.set_ylabel('EjeY')
ax2.plot(range(8),[0.8,0.6,0.4,0.2,0.1,0.3,0.5,0.7],'green',1.5, label='this')
ax2.legend()

ax3 = fig.add_subplot(2,1,2,axisbg='#cccccc')	#graph color
ax3.tick_params(axis='x', colors='black')	#grid lines color
ax3.tick_params(axis='y', colors='black')
ax3.spines['bottom'].set_color('black')	#margin color
ax3.spines['top'].set_color('black')
ax3.spines['left'].set_color('black')
ax3.spines['right'].set_color('black')
ax3.xaxis.label.set_color('black')	#labels color
ax3.yaxis.label.set_color('black')
ax3.set_title('matplotlip ttl',color='black')
ax3.set_xlabel('EjeX')
ax3.set_ylabel('EjeY')
ax3.plot(range(8),range(8), label='uno')
ax3.plot(range(8),range(8)[::-1], label='dos')
ax3.plot(range(8),[6,1,5,2,4,3,5,1],'red',1.5, label='tres')
ax3.legend()

plt.show()
