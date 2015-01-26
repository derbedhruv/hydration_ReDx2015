import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.signal import argrelmax

x = np.arange(0,1200);
SineLowFreq = 2.5*np.sin(x * 0.01 * np.pi);
SineMedFreq = 0.5 * np.sin(x * 0.01 * np.pi * 5);
SineHighFreq = 0.9*np.sin(x * 0.01 * np.pi * 12);
data = 30 + SineLowFreq + SineMedFreq + SineHighFreq;
plt.plot(x,data)
plt.ylim(20,40)
plt.show()
#print data
#print x
z = sp.signal.argrelmax(data)
for i in range (0,len(z)):
    data = data[z[i]]

#print data

u = sp.signal.argrelmax(data)
for i in range (0,len(u)):
    data = data[u[i]]
    
print data


