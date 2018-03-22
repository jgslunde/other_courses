import numpy as np
import matplotlib.pyplot as plt

c = 1.
mE = 600.0
mD = 500.0
mC = 200.0
mB = 150.0
mA = 100.0
ma = mb = 1.8
md = mc = 0

PaB = np.zeros(3) #four-momentum for paricle a, seen from B RF
PbC = np.zeros(3)
PcD = np.zeros(3)
Pd = np.zeros(3)

LB = np.zeros((3,3)) #Transformation from RF B to RF C
LC = np.zeros((3,3)) #Transformation from RF C to RF D
LD = np.zeros((3,3)) #Transformation from RF D to RF E


pd = c*(mE**2 - mD**2)/(2*mE)               #Relativistic momentum of particle d in RF E
vD = pd/(mD*np.sqrt(1 + pd**2/(mD*c)**2))   #Velocity of particle D in RF E

pc = c*(mD**2 - mC**2)/(2*mD)               #Relativistic momentum of particle c in RF D
vC = pc/(mC*np.sqrt(1 + pc**2/(mC*c)**2))   #Velocity of particle C in RF D

pb = c*np.sqrt(mB**4 - 2*mB**2*mb**2 - 2*mB**2*mC**2 + mb**4 - 2*mb**2*mC**2 + mC**4)/(2*mC)    #Relativistic momentum of particle b in RF C
vB = pb/(mC*np.sqrt(1 + pb**2/(mC*c)**2))

pa = c*np.sqrt(mA**4 - 2*mA**2*ma**2 - 2*mA**2*mB**2 + ma**4 - 2*ma**2*mB**2 + mB**4)/(2*mB)    #Velocity of particle B in RF C

gammaD = 1/np.sqrt(1 - vD**2/c**2)
gammaC = 1/np.sqrt(1 - vC**2/c**2)
gammaB = 1/np.sqrt(1 - vB**2/c**2)

def M2xy(x,y):
    return (x[0] + y[0])**2 - ((x[1] + y[1])**2 + (x[2] + y[2])**2)


N = 10000
M2 = np.zeros(N)
test = np.zeros(N)
for i in xrange(N):

    atheta = np.random.uniform(0,2*np.pi)
    btheta = np.random.uniform(0,2*np.pi)
    ctheta = np.random.uniform(0,2*np.pi)
    dtheta = np.random.uniform(0,2*np.pi)
    """
    Constructing the Lorentz matrix to boost from RF D to E
    """
    LD[0,0] = gammaD
    LD[1,1] = 1 + (gammaD - 1)*np.cos(dtheta + np.pi)**2
    LD[2,2] = 1 + (gammaD - 1)*np.sin(dtheta + np.pi)**2
    LD[0,1] = LD[1,0] =  gammaD*vD*np.cos(dtheta + np.pi)/c
    LD[0,2] = LD[2,0] =  gammaD*vD*np.sin(dtheta + np.pi)/c
    LD[1,2] = LD[2,1] =  (gammaD - 1)*np.sin(dtheta + np.pi)*np.cos(dtheta + np.pi)

    LC[0,0] = gammaC
    LC[1,1] = 1 + (gammaC - 1)*np.cos(ctheta + np.pi)**2
    LC[2,2] = 1 + (gammaC - 1)*np.sin(ctheta + np.pi)**2
    LC[0,1] = LC[1,0] =  gammaC*vC*np.cos(ctheta + np.pi)/c
    LC[0,2] = LC[2,0] =  gammaC*vC*np.sin(ctheta + np.pi)/c
    LC[1,2] = LC[2,1] =  (gammaC - 1)*np.sin(ctheta + np.pi)*np.cos(ctheta + np.pi)

    LB[0,0] = gammaB
    LB[1,1] = 1 + (gammaB - 1)*np.cos(btheta + np.pi)**2
    LB[2,2] = 1 + (gammaB - 1)*np.sin(btheta + np.pi)**2
    LB[0,1] = LB[1,0] =  gammaB*vB*np.cos(btheta + np.pi)/c
    LB[0,2] = LB[2,0] =  gammaB*vB*np.sin(btheta + np.pi)/c
    LB[1,2] = LB[2,1] =  (gammaB - 1)*np.sin(btheta + np.pi)*np.cos(btheta + np.pi)

    Pd[0] = pd                  #four-momentum of d in RF E
    Pd[1] = pd*np.cos(dtheta)
    Pd[2] = pd*np.sin(dtheta)

    PcD[0] = pc                #four-momentum c in RF D
    PcD[1] = pc*np.cos(ctheta)
    PcD[2] = pc*np.sin(ctheta)

    PbC[0] = np.sqrt(pb**2 + mb**2*c**2)                #four-momentum of b in RF C
    PbC[1] = pb*np.cos(btheta)
    PbC[2] = pb*np.sin(btheta)

    PaB[0] = np.sqrt(pa**2 + ma**2*c**2)                #four-momentum of a in RF B
    PaB[1] = pa*np.cos(atheta)
    PaB[2] = pa*np.sin(atheta)

    Pc = np.dot(LD,PcD)                                 #transforming four-momentum of c in D to E
    Pb = np.dot(np.dot(LD,LC) , PbC)                    #transforming four-momentum of b in C to D, then to E
    Pa = np.dot(np.dot(np.dot(LD,LC), LB) , PaB)        #transforming four-momentum of a in B to C, then D, then E

    Mdc[i] = M2xy(Pd,Pc)                                 #Calculating the invarient mass squared
    Mdb[i] = M2xy(Pd,Pb)
    Mda[i] = M2xy(Pd,Pa)
    Mcb[i] = M2xy(Pc,Pb)
    Mca[i] = M2xy(Pc,Pa)
    Mba[i] = M2xy(Pb,Pa)
    test[i] = (mD**2 - mC**2)*(mE**2 - mD**2)/(2*mD**2)*(1 -np.cos(dtheta))      #Analytical solution


plt.hist(Mdc)
plt.show()
plt.hist(Mdb)
plt.show()
plt.hist(Mda)
plt.show()
plt.hist(Mcb)
plt.show()
plt.hist(Mca)
plt.show()
plt.hist(Mba)
plt.show()

#plt.hist(test)
#plt.show()
