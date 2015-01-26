import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.signal import argrelmax

#file_time=open("C:\Users\nithin\Documents\pythonRedx\850nm1minData.txt","r")
#file_value=open("C:/Users/Divya/Documents/RedX/Filters/value.txt","r")

#time = [ map(float,line.split('  ')) for line in file_time ]
#value = 50+[ map(float,line.split('  ')) for line in file_value ]
#lines = [line.strip() for line in open("C:\\Users\\nithin\\Documents\\pythonRedx\\850nm1minData.txt","r")]
lines = [line.rstrip('\n').split('	') for line in open("C:\Users\Divya\Documents\RedX\hydration_ReDx2015\Divya\Sample_data_without_headers\850nm-1minData_2.txt","r")]
#print lines
print len(lines)

#print lines[50003][1]
time = np.zeros((50004, 1))
data = np.zeros((50004, 1))
for i in range(0,len(lines)):
    time[i] = lines[i][1]
    data[i] = lines[i][0]    
#print data   