import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

#euklidiselle laskennalle funktio
def etaisyys(p1, p2):
    e = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
    e = math.sqrt(e)
    return(e)

#perus plussa lasku funktio jossa xyz + xyz
def plussaus(arvo1, arvo2):
    ar1 = (arvo1[0]+arvo2[0]),(arvo1[1]+arvo2[1]),(arvo1[2]+arvo2[2])
    return(ar1)

url = "http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=74"
csv = pd.read_csv(url, delimiter=';')
csv.to_csv('groupid74data.csv')

#p = np.loadtxt("putty.log")
p = pd.read_csv("groupid74data.csv")

numberOfRows = int(len(p)/3) #jaetaan putty log 3 osaan int(len(r)/3)


print("rivien lukumäärä =",numberOfRows)
    
data = np.zeros((numberOfRows,3))#määritellään putty log datalle x y ja z akselit
data[:,0]=p[0:len(p):3]
data[:,1]=p[1:len(p):3]
data[:,2]=p[2:len(p):3]
print(data)
print("")

x = data[:,0]=p[0:len(p):3]
y = data[:,1]=p[1:len(p):3]
z = data[:,2]=p[2:len(p):3]

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x,y,z)
plt.show()
"""
luetaan array data amaxilla ja sitten arvotaan
0-datan maksimin välillä
randint antaa kokonaisluvun koska random.rand antaa sen floattina ja anna rationaalilukua esim 1.743434343
"""
f = np.amax(data)
kp = np.random.randint(0,f, size=(4,3))

print("keskipisteet", kp)
print("")

cpcs = np.zeros((4,3))
counts = np.zeros(4)
distances = np.zeros(4)

for l in range(4):
    if counts[l] == 0:
        kp[l,:] = np.random.randint(0,f, size=(3))
    else:
        kp[l,:] = cpcs[l,:]/counts[l]

for i in range(numberOfRows):
    for j in range(4):
        distances[j]=etaisyys(data[i,:], kp[j,:])

    voittaja = np.argmin(distances)
    # counts[voittaja]=counts[voittaja]+1
    counts[voittaja] += 1
    # cpcs[voittaja]=plussaus(cpcs[voittaja], data[i,:])
    cpcs[voittaja] += data[i,:]

#tehdään projektin kohdat 1 ja 2 ja tallennetaan joka kerralla
#kun lasketaan uudet kp eli kp x10
for g in range(10):
    rakenne = np.zeros((4,3))
    p = np.loadtxt("putty.log")
    numberOfRows = int(len(p)/3)
    data = np.zeros((numberOfRows,3))
    data[:,0]=p[0:len(p):3]
    data[:,1]=p[1:len(p):3]
    data[:,2]=p[2:len(p):3]
    f = np.amax(data)
    kp = np.random.randint(0,f, size=(4))
    print(kp, "uudet kp")
    
print("")
print("counts", distances)
print("")
print("distances", counts)
print("")
print("cumulative", cpcs)
print("")