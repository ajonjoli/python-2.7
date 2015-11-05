from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
X, Y, Z = range(6), [5,6,3,1,5,2], [8,7,6,8,7,5]
X2, Y2, Z2 = [2,3,4,5,6,7], [5,6,3,1,5,2], range(6)
X3, Y3, Z3 = [5,6,3,1,5,2], range(6), [2,3,4,5,6,7]
X, Y, Z = axes3d.get_test_data(0.05)	#every axe gets a matrix
#print len(X),X[0]

#bar charts
#xpos=range(1,11)	#origin of points
#ypos=[2,3,4,5,1,6,2,1,7,2]
#zpos=[0]*10
#zpos[4]=4
#dx=[1]*10	#distance to move on directions
#dy=[1]*10
#dz=range(1,11)

#ax.plot_wireframe(X,Y,Z)	#one line
#ax.scatter(X,Y,Z, c='green', marker='o')	#only dots
#ax.scatter(X2,Y2,Z2, c='red', marker='v')	#only dots
#ax.scatter(X3,Y3,Z3, c='blue', marker='^')	#only dots
#ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ccaa')	#3d bars
ax.plot_wireframe(X,Y,Z, rstride=5, cstride=2)	#planos 3d

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.show()

