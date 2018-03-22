import numpy as np
import matplotlib.pyplot as plt

c = 1.0
mE = 600.0
mD = 500.0
mC = 200.0
mB = 150.0
mA = 100.0
ma = mb = 1.8
md = mc = 0

PaB = np.zeros(4) #four-momentum for paricle a, seen from B RF
PbC = np.zeros(4)
PcD = np.zeros(4)
Pd = np.zeros(4)

L = np.zeros((4,4,4)) #Transformation from RF B to RF C

pd = c*(mE**2 - mD**2)/(2*mE)               #Relativistic momentum of particle d in RF E
vD = pd/(mD*np.sqrt(1 + pd**2/(mD*c)**2))   #Velocity of particle D in RF E

pc = c*(mD**2 - mC**2)/(2*mD)               #Relativistic momentum of particle c in RF D
vC = pc/(mC*np.sqrt(1 + pc**2/(mC*c)**2))   #Velocity of particle C in RF D

pb = c*np.sqrt(mB**4 - 2*mB**2*mb**2 - 2*mB**2*mC**2 + mb**4 - 2*mb**2*mC**2 + mC**4)/(2*mC)    #Relativistic momentum of particle b in RF C
vB = pb/(mB*np.sqrt(1 + pb**2/(mB*c)**2))

pa = c*np.sqrt(mA**4 - 2*mA**2*ma**2 - 2*mA**2*mB**2 + ma**4 - 2*ma**2*mB**2 + mB**4)/(2*mB)    #Velocity of particle B in RF C
vA = pa/(mA*np.sqrt(1 + pa**2/(mA*c)**2))

v = np.array((vD,vC,vB,vA))
gamma = 1/np.sqrt(1 - v**2/c**2)

def M2xy(x,y):
    return (x[0] + y[0])**2 - ((x[1] + y[1])**2 + (x[2] + y[2])**2 + (x[3] + y[3])**2)

N = 10000
M2 = np.zeros((N,6))
test = np.zeros(N)

for i in xrange(N):
    phi = np.random.uniform(0,2*np.pi,4); theta = np.arccos(np.random.uniform(-1,1,4))
    L[0,0] = gamma
    L[1,1] = 1 + (gamma - 1)*(np.cos(phi + np.pi)*np.sin(-theta + np.pi))**2
    L[2,2] = 1 + (gamma - 1)*(np.sin(phi + np.pi)*np.sin(-theta + np.pi))**2
    L[3,3] = 1 + (gamma - 1)*np.cos(-theta + np.pi)**2

    L[0,1] = L[1,0] =  gamma*v*np.cos(phi + np.pi)*np.sin(-theta + np.pi)/c
    L[0,2] = L[2,0] =  gamma*v*np.sin(phi + np.pi)*np.sin(-theta + np.pi)/c
    L[0,3] = L[3,0] =  gamma*v*np.cos(-theta + np.pi)/c

    L[1,2] = L[2,1] =  (gamma - 1)*np.cos(phi + np.pi)*np.sin(phi + np.pi)*np.sin(-theta + np.pi)**2
    L[1,3] = L[3,1] =  (gamma - 1)*np.cos(phi + np.pi)*np.sin(-theta + np.pi)*np.cos(-theta + np.pi)
    L[2,3] = L[3,2] =  (gamma - 1)*np.sin(phi + np.pi)*np.sin(-theta + np.pi)*np.cos(-theta + np.pi)

    Pd[0] = pd                  #four-momentum of d in RF E
    Pd[1] = pd*np.cos(phi[0])*np.sin(theta[0])
    Pd[2] = pd*np.sin(phi[0])*np.sin(theta[0])
    Pd[3] = pd*np.cos(theta[0])

    PcD[0] = pc                 #four-momentum c in RF D
    PcD[1] = pc*np.cos(phi[1])*np.sin(theta[1])
    PcD[2] = pc*np.sin(phi[1])*np.sin(theta[1])
    PcD[3] = pc*np.cos(theta[1])

    PbC[0] = np.sqrt(pb**2 + mb**2*c**2)                #four-momentum of b in RF C
    PbC[1] = pb*np.cos(phi[2])*np.sin(theta[2])
    PbC[2] = pb*np.sin(phi[2])*np.sin(theta[2])
    PbC[3] = pb*np.cos(theta[2])

    PaB[0] = np.sqrt(pa**2 + ma**2*c**2)                #four-momentum of a in RF B
    PaB[1] = pa*np.cos(phi[3])*np.sin(theta[3])
    PaB[2] = pa*np.sin(phi[3])*np.sin(theta[3])
    PaB[3] = pa*np.cos(theta[3])

    Pc = np.dot(L[:,:,0], PcD)                                           #transforming four-momentum of c in D to E
    Pb = np.dot(np.dot(L[:,:,0],L[:,:,1]), PbC)                           #transforming four-momentum of b in C to D, then to E
    Pa = np.dot(np.dot(np.dot(L[:,:,0],L[:,:,1]), L[:,:,2]), PaB)        #transforming four-momentum of a in B to C, then D, then E

    M2[i,0] = M2xy(Pa,Pb)                                                #Calculating the invarient mass squared
    M2[i,1] = M2xy(Pa,Pc)
    M2[i,2] = M2xy(Pa,Pd)
    M2[i,3] = M2xy(Pb,Pc)
    M2[i,4] = M2xy(Pb,Pd)
    M2[i,5] = M2xy(Pc,Pd)
    #test[i] = (mD**2 - mC**2)*(mE**2 - mD**2)/(2*mD**2)*(1 -np.cos(theta[0]))      #Analytical solution

#for i in xrange(6):
#    plt.hist(np.sqrt(M2[:,i]),50)
#    plt.show()


y, binEdges = np.histogram(M2[:,0],bins=50)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
plt.plot(bincenters,y,'-', label="m_ab")

y, binEdges = np.histogram(M2[:,1],bins=50)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
plt.plot(bincenters,y,'-', label="m_ac")

y, binEdges = np.histogram(M2[:,2],bins=50)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
plt.plot(bincenters,y,'-', label="m_ad")

y, binEdges = np.histogram(M2[:,3],bins=50)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
plt.plot(bincenters,y,'-', label="m_bc")

y, binEdges = np.histogram(M2[:,4],bins=50)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
plt.plot(bincenters,y,'-', label="m_bd")

y, binEdges = np.histogram(M2[:,5],bins=50)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
plt.plot(bincenters,y,'-', label="m_cd")

plt.legend()
plt.savefig("stuff1.png")

# print(np.shape(M2))
print(np.max(M2[:,0]))

# plt.hist(M2[:,0], 100)
# plt.show()
# plt.hist(M2[:,1], 100)
# plt.show()
# plt.hist(M2[:,2], 100)
# plt.show()
# plt.hist(M2[:,3], 100)
# plt.show()
# plt.hist(M2[:,4], 100)
# plt.show()
# plt.hist(M2[:,5], 100)
# plt.show()

# plt.plot(np.sqrt(M2[:,0]))
# plt.plot(np.sqrt(M2[:,1]))
# plt.plot(np.sqrt(M2[:,2]))
# plt.plot(np.sqrt(M2[:,3]))
# plt.plot(np.sqrt(M2[:,4]))
# plt.plot(np.sqrt(M2[:,5]))



plt.figure()
plt.subplot(3,1,1)
plt.hist(M2[:,0],50)
plt.xlabel('$ m_{ab}^2 $')
plt.ylabel("$ Counts $")

plt.subplot(3,1,2)
plt.hist(M2[:,1],50)
plt.xlabel('$ m_{ac}^2 $')
plt.ylabel("$ Counts $")

plt.subplot(3,1,3)
plt.hist(M2[:,2],50)
plt.xlabel('$ m_{ad}^2 $')
plt.ylabel("$ Counts $")

plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=None, hspace=0.9)

plt.savefig("stuff2.png")

plt.subplot(3,1,1)
plt.hist(M2[:,3],50)
plt.xlabel('$ m_{bc}^2 $')
plt.ylabel("$ Counts $")

plt.subplot(3,1,2)
plt.hist(M2[:,4],50)
plt.xlabel('$ m_{bd}^2 $')
plt.ylabel("$ Counts $")

plt.subplot(3,1,3)
plt.hist(M2[:,0],50)
plt.xlabel('$ m_{cd}^2 $')
plt.ylabel("$ Counts $")

plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=None, hspace=0.9)


plt.savefig("stuff3.png")

#a = np.array([[1,2],[3,4]])
#print a[:,1]
