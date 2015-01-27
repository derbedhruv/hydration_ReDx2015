import math
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from numpy import *

from scipy.signal import butter, lfilter
from scipy.signal import freqs

filename="C:\Users\Divya\Documents\RedX\Filters\\values_30sec.txt"
#filename="C:\Users\Divya\Documents\RedX\Filters\\value.txt"
lines= [line.rstrip('\n') for line in open(filename,"r")]

s=len(lines)

time = np.zeros((s, 1))
data = np.zeros((s, 1))
for i in range(0,s):
    time[i] = i
    data[i] = lines[i]#[1]  

s=len(data)
print s

print data

sample=data[0]
filtered_value1=np.zeros((s, 1))
filtered_value2=np.zeros((s, 1))
filtered_value3=np.zeros((s, 1))

print "Starting now"

i=1
while i<s:
    last_sample=sample;
    sample=data[i]
    filtered_value1[i] = filtered_value1[i-1] + 0.0001 * (data[i-1]- filtered_value1[i-1])+0.00007*(data[i-2] - filtered_value1[i-2])+0.00002*(data[i-3] - filtered_value1[i-3])+0.000005*(data[i-4] - filtered_value1[i-4])
    i=i+1
    

o = data - filtered_value1
    
print "Plotting output"

#print filtered_value

#plt.subplots(1,1)

cutOff = 2*math.pi*0.5 #23.1 #cutoff frequency in rad/s
fs = 2*math.pi*50#188.495559 #sampling frequency in rad/s
order = 4 #order of filter

#fil_value = butter_lowpass_filter(data, cutOff, fs, order)
#plt.plot(time,fil_value,'b')


plot(time,data,'c')
#plt.show()
#subplots(3,1,1)
plot(time,filtered_value1,'g')
#subplot(3,1,2)
plot(time,o,'r')
#subplot(3,1,3)
plt.show()

print "End"