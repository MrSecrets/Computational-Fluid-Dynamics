import numpy as np

from matplotlib import pyplot as plt
data=np.loadtxt('surfaceFieldValue.dat')
X=data[:,0]
Y=data[:,1]
Y=(360/5)*Y
b=np.gradient(Y)
plt.figure(1)
plt.plot(X,Y,':ro')
legend=plt.legend(loc='upper right',shadow=True)
plt.ylabel('Concentration(T)')
plt.xlabel('Time(s)')
plt.grid('on')
plt.title('Variation of Concentration')
plt.savefig('Concentration.eps')
plt.show()
plt.figure(2)
plt.plot(X,b,':ro')
legend=plt.legend(loc='upper right',shadow=True)
plt.ylabel('Gradient of Concentration(T)')
plt.xlabel('Time(s)')
plt.grid('on')
plt.title('RTD Plot')
plt.savefig('RTD.eps')
plt.show()
