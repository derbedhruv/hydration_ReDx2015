from fnmatch import fnmatch, fnmatchcase
import os
from Tkinter import *
import datetime

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
filesearchname="%s%s%s_%s_*.txt" % (date.year,date.month,date.day,e1.get()) #"20150127_%s_*.txt"%(e1.get())
print (filesearchname)

for path,subdirs,files in os.walk('C:/Users/Divya/Documents/RedX/hydration_ReDx2015/Divya/log'):
    for filename in files:
        print (filename)
        if fnmatch(filename,filesearchname):
            count=count+1
            
count=count + 1 #count to be appended
print (count)


newfilename = "C:/Users/Divya/Documents/RedX/hydration_ReDx2015/Divya/log/%s%s%s_%s_%d.txt" % (date.year,date.month,date.day,e1.get(),count)
print (newfilename)

f = open(newfilename,"a") #opens file with name of "test.mtxt"
f.write("Name:" + e1.get() + "\n")
f.write("Age:" + e2.get() + "\n")
f.write("Remarks:" + e3.get() + "\n")
#f.write("Maybe someday, he will promote me to a real file.")
#f.write("Man, I long to be a real file")
#f.write("and hang out with all my new real file friends.") 

#SERIAL COMMUNICATION COMES HERE!!!!!!!!!!!!!!!!


#END OF SERIAL COMMUNICATION

f.close()



