'''
  This file takes details about a patient and then reads in csv data from an arduino UNO 
  and puts the data into a text file which will carry the patients name and the date.
  
  Authors: Divya Ramnath, Nithin Sankar K, Shoubhik Deb, Dhruv Joshi
  
  Done as part of the 2015 ReDx workshop at IIT Bombay organized by the camera culture group, MIT Media Lab.
  
'''
from fnmatch import fnmatch, fnmatchcase
import os
from Tkinter import *
import datetime
import serial
import os

#print lines
#print len(lines)

#print lines[50003][1]


def show_entry_fields():
   print("Name: %s\nAge: %s\nRemarks: %s" % (e1.get(), e2.get(), e3.get()))

master = Tk()
Label(master, text="Name").grid(row=0)
Label(master, text="Age").grid(row=1)
Label(master, text="Remarks").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Submit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Display', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )


date=datetime.datetime.now()
print (date)
count = 0

# check if the current file exists in path, if so then increase count which will be appended
while os.path.exists("%s%s%s_%s_%d.txt" % (date.year,date.month,date.day,e1.get(),count)):
    count += 1

newfilename = "%s%s%s_%s_%d.txt" % (date.year,date.month,date.day,e1.get(),count)
# print (newfilename)

f = open(newfilename,"a") #opens file with name of "test.mtxt"
f.write("Name:" + e1.get() + "\n")
f.write("Age:" + e2.get() + "\n")
f.write("Remarks:" + e3.get() + "\n")
#f.write("Maybe someday, he will promote me to a real file.")
#f.write("Man, I long to be a real file")
#f.write("and hang out with all my new real file friends.") 

time = sampling_rate*samples

#SERIAL COMMUNICATION COMES HERE!!!!!!!!!!!!!!!!
arduino = serial.Serial('COM23', 115200, timeout=1)

for i in range(0, time):
  data = arduino.readline()
  f.write(data)

#END OF SERIAL COMMUNICATION

f.close()



