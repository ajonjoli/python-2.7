import pylab #import *

pos = pylab.arange(6)+0.5
#print pos,type(pos)
pylab.barh(pos, (3,5,2,1,2,9), align='center', color='#00ff5c')
pylab.yticks(pos, ('Paul', 'Hillary', 'Marco', 'Tedd', 'Sanct', 'Kerry'))
pylab.xlabel('Sentiment Index')
pylab.ylabel('candidates')
pylab.title('Prezdex')
pylab.grid(True)
pylab.subplots_adjust(left=.20, right=.97)	#adjust config params

pylab.show()
