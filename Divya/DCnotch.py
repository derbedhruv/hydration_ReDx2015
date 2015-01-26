import math
import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import butter, lfilter
from scipy.signal import freqs
filename="C:\Users\Divya\Documents\RedX\hydration_ReDx2015\Divya\Sample_data_without_headers\\20140522-0002_2.txt"
lines= [line.rstrip('\n').split('	') for line in open(filename,"r")]

s=len(lines)
print s

time = np.zeros((s, 1))
data = np.zeros((s, 1))
for i in range(0,s):
    time[i] = lines[i][0]
    data[i] = lines[i][1]  


sample=data[0] +50
filtered_value=np.zeros((s, 1))


print "Starting now"

i=1
while i<s:
    last_sample=sample;
    sample=data[i] + 50
    filtered_value[i] = 0.996 * (filtered_value[i-1] + sample - last_sample)
    i=i+1

print "Plotting output"
print 'filtered_value =',len(filtered_value)
print filtered_value

plt.plot(time,data,'r')

plt.plot(time,filtered_value,'g')

plt.show()
print "End"