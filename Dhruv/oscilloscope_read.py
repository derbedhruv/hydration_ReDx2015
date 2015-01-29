# we;re going to extrat data from the oscilloscope and put it into proper variables for monitoring later
import numpy, matplotlib

f = open('data.txt')	# open the file saved by the oscilloscope
header_lines = 7

data = f.readlines()

chanA = []
chanB = []

for i in range(header_lines, len(d)):
  dline = data[i].split(",")
  
  # put the data in
  chanA.append((int)dline[0].strip())
  chanB.append((int)dline[1].strip())
  
# Now we have the data in the form of 2 channels .. needs to be processed