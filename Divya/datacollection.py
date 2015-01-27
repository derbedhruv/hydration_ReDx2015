#var = raw_input("Please enter your name: ")
#print "you entered", var

from Tkinter import *

#top = Tk()
#L1 = Label(top, text="User Name")
#L1.pack( side = LEFT)
#E1 = Entry(top, bd =5)

#E1.pack(side = RIGHT)

#top.mainloop()

from Tkinter import *

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

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )

f = open("C:/Users/Divya/Documents'/RedX/hydration_ReDx2015/Divya/test.txt","a") #opens file with name of "test.txt"
f.write("Name:" + e1.get() + "\n")
f.write("Age:" + e2.get() + "\n")
f.write("Remarks:" + e3.get() + "\n")
#f.write("Maybe someday, he will promote me to a real file.")
#f.write("Man, I long to be a real file")
#f.write("and hang out with all my new real file friends.") 
f.close()
