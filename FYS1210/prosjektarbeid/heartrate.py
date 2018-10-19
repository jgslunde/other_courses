# -*- coding utf8 -*-
import numpy as np
import matplotlib.pylab as plt

time = np.linspace(0,190,20)


puls = np.array([58,57,57,56,60,67,64,56,75,97,105,107,95,96,100,91,83,73,67,61])

plt.plot(time,puls)
plt.axvline(70, linestyle = "--", color = "0.75", label = "start trening ")
plt.axvline(140, linestyle = "--", color = "0.75", label = "stopp trening")
plt.legend(loc="best")
plt.xlabel("Tid [sek]")
plt.ylabel("Puls [slag/min]")
plt.savefig("fig/heartrate.pdf")
plt.clf()


frekvens = np.array([1,10,100,1000])
konduktans = np.array([58,55.6, 60, 62 ])*1e-6
suseptans = np.array([38,36.13,41, 48])*1e-6
admittans = np.sqrt(suseptans**2 + konduktans**2)
print "Admittans = ", admittans*1e6


plt.loglog(frekvens, konduktans, label = "konduktans")
plt.loglog(frekvens, suseptans, label = "suseptans ")
plt.axis([0,1e3,1e-5,1e-4])
plt.legend(loc= "best")
plt.xlabel("Frekvens [Hz]")
plt.ylabel("Admittans [Siemens]")
plt.savefig("fig/admittance.pdf")
plt.clf()
