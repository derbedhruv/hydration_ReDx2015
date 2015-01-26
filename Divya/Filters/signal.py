import math
import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import butter, lfilter
from scipy.signal import freqs

file_time=open("C:\Users\Divya\Documents\RedX\Filters\\time.txt","r")
file_value=open("C:/Users/Divya/Documents/RedX/Filters/value.txt","r")
#time=open(file_time,'r')
#value=open(file_value,'r')
time = [ map(float,line.split('  ')) for line in file_time ]
value = 50+[ map(float,line.split('  ')) for line in file_value ]

#print(time)

t=0.1

k=0

#t = np.arange(0,10,0.01)
#y=[0]*1000
yy=[0]*1000

#final=[0]*1000
final_actual=[0]*1000
#x=np.sin(2*math.pi*t)+np.sin(4*math.pi*t)+np.sin(6*math.pi*t)+np.sin(8*math.pi*t)+np.sin(10*math.pi*t)
#x=50+np.sin(2*math.pi*t)+np.sin(4*math.pi*t)+np.sin(10*math.pi*t)
#x=value
#t=time
x=value
t=time
#print x
#print t
s=len(x)
final=[0]*s
y=[0]*s

#print s

#while k<1000:
#    y[k]=(x[k]+x[k-1]+x[k-2]+x[k-3])/4
    #y[k+3]=(2.914649446574e-5 * x[k]) + (  0.8818931306 * y[k]) + ( -2.7564831952 * y[k+1]) + (  2.8743568927 * y[k+2]);
#    k=k+1

#plt.plot(t,x)
#plt.ylim((-100,100))	
	
#plt.show()

def butter_lowpass(cutOff, fs, order):
    nyq = 0.5 * fs
    normalCutoff = cutOff / nyq
    b, a = butter(order, normalCutoff, btype='low', analog = True)
    return b, a

def butter_lowpass_filter(value, cutOff, fs, order):
    b, a = butter_lowpass(cutOff, fs, order)
    y = lfilter(b, a, value)
    return y

cutOff = 2*math.pi*2 #23.1 #cutoff frequency in rad/s
fs = 2*math.pi*50#188.495559 #sampling frequency in rad/s
order = 2 #order of filter

#print sticker_data.ps1_dxdt2

#decent (source: http://www.schwietering.com/jayduino/filtuino/index.php?characteristic=bu&passmode=lp&order=3&usesr=usesr&sr=50&frequencyLow=2&noteLow=&noteHigh=&pw=pw&calctype=float&run=Send)
#while k<998:
    #y[k] = y[k+1]
    #y[k+1] = (1.121602444752e-1 * x[k]) + (  0.7756795110 * y[k]);
    #final[k]=y[k]+y[k+1]
    #k=k+1
    
    #y[k] = y[k+1]
    #y[k+1] = y[k+2]
    #y[k+2] = (1.335920002786e-2 * x[k]) + ( -0.7008967812 * y[k]) + (  1.6474599811 * y[k+1])
    #final[k] = y[k] + y[k+2] + 2 * y[k+1]
    #k=k+1
    
    #consider using long for faster computation! The option is available on the above mentioned website
    
    #yy[k] = y[k+1]
    #yy[k+1]=y[k+2]
    #yy[k+2]=y[k+3]
    #yy[k+3] = (1.567010350588e-3 * x[k])+ (  0.6041096995 * y[k]) + ( -2.1152541270 * y[k+1])+ (  2.4986083447 * y[k+2]);
    #final[k]=(y[k] + y[k+3]) +3 * (y[k+1] + y[k+2])
    #k=k+3
    

#final_actual = butter_lowpass_filter(x, cutOff, fs, order)
#plt.plot(t,final_actual,'b')
#plt.plot(t,final,'r')

y = butter_lowpass_filter(x, cutOff, fs, order)


plt.plot(time,value,'b')

#plt.plot(time,y,'g')	
plt.show()

