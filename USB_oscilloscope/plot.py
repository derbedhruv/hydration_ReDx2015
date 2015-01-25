import matplotlib.pyplot as plt
import numpy

fileName = "2014116.csv"		# change name of file to suit needs

sampling_rate = 100.0		# enter in Hz, decimal point is essential
deltat = 1/sampling_rate

data = numpy.genfromtxt(fileName, unpack=True)

t = numpy.arange(0, deltat*len(data), deltat)		# create a fake time axis in seconds

plt.plot(t, data)				# plot the suckers
plt.show()