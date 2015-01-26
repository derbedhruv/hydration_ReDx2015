import numpy as np
import matplotlib.pyplot as plt

filename="C:\Users\Divya\Documents\RedX\hydration_ReDx2015\Divya\Sample_data_without_headers\\20140522-0002_2.txt"
lines= [line.rstrip('\n').split('	') for line in open(filename,"r")]

s=len(lines)
print s

time = np.zeros((s, 1))
data = np.zeros((s, 1))
for i in range(0,s):
    time[i] = lines[i][0]
    data[i] = lines[i][1]  



input = np.array([ 1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1. ,  1.1,  1. ,  0.8,  0.9,
    1. ,  1.2,  0.9,  1. ,  1. ,  1.1,  1.2,  1. ,  1.5,  1. ,  3. ,
    2. ,  5. ,  3. ,  2. ,  1. ,  1. ,  1. ,  0.9,  1. ,  1. ,  3. ,
    2.6,  4. ,  3. ,  3.2,  2. ,  1. ,  1. ,  1. ,  1. ,  1. ])
signal = (data > np.roll(data,1)) & (data > np.roll(data,-1))
plt.plot(data,'k')
plt.plot(signal.nonzero()[0], data[signal], 'ro')
plt.show()