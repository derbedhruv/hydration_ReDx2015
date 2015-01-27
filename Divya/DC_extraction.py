import math
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from numpy import *
import Tkinter


filename="C:/Users/Divya/Documents/RedX/hydration_ReDx2015/Divya/Sample_data_without_headers/20140522-0002_2.txt"
lines= [line.rstrip('\n').split('	') for line in open(filename,"r")]

s=len(lines)
print (s)

time = np.zeros((s, 1))
data = np.zeros((s, 1))
for i in range(0,s):
    time[i] = lines[i][0]
    data[i] = lines[i][1]  


sample=data[0]
filtered_value1=np.zeros((s, 1))-1.1
filtered_value2=np.zeros((s, 1))
filtered_value3=np.zeros((s, 1))

print ("Starting now")

i=1
while i<s:
    last_sample=sample;
    sample=data[i]
    filtered_value1[i] = filtered_value1[i-1] + 0.0002 * (data[i-1]- filtered_value1[i-1])+0.00007*(data[i-2] - filtered_value1[i-2])+0.00002*(data[i-3] - filtered_value1[i-3])+0.000005*(data[i-4] - filtered_value1[i-4])
    
    #plot(time[i],filtered_value1[i],'g')
    #plt.show()
    i=i+1
    
    

o = data - filtered_value1
    
print ("Plotting output")



plot(time,data,'c')
#plt.show()
#subplots(3,1,1)
plot(time,filtered_value1,'g')
#subplot(3,1,2)
plot(time,o,'r')
#subplot(3,1,3)
plt.show()

print ("End")