import math
import cmath
from scipy.special import jv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
r=39
a=0.25
varz=0.1
z=1
E0=5
k=0.05
lambd=1000*10**-9
centers=[[-r/2,r/2],[-r/2,-r/2],[r/2,r/2],[r/2,-r/2]]
def getc(x,y):
    return math.exp((k*((x*z)**2+(y*z)**2))/(2*z))/(lambd*z)

def e(x,y,id):
    val=math.sqrt(x**2+y**2)
    return math.pi*a*a*getc(x,y)*E0*math.exp(-k*(x*centers[id][0]+y*centers[id][1]))*2*jv(2, k*a*(val if val!=0 else 0.08))/(val if val!=0 else 1)

def getarr(id):
    return [[1/e(i/1000,j/1000,id) for j in range (-10,11)] for i in range(10,-11,-1)]
fig1, ax1 = plt.subplots(nrows=1, ncols=1)
fig2, ax2 = plt.subplots(nrows=1, ncols=1)

arr0=getarr(0)
arr1=getarr(1)
arr2=getarr(2)
arr3=getarr(3)
arrx=[arr0[i]+arr1[i] for i in range(len(arr0))]+[arr2[i]+arr3[i] for i in range(len(arr0))]
ax2.imshow(arrx, cmap='turbo', interpolation='nearest')

def update1(frame):
    global k,lambd,varz,z
    #lambd+=10*10**-9
    #k+=0.05
    z=1
    arr0=getarr(0)
    arr1=getarr(1)
    arr2=getarr(2)
    arr3=getarr(3)
    arrx=[arr0[i]+arr1[i] for i in range(len(arr0))]+[arr2[i]+arr3[i] for i in range(len(arr0))]
    ax1.imshow(arrx, cmap='turbo', interpolation='nearest')
    print(z)
c=1
def update2(frame):
    global k,lambd,varz,z,c
    lambd+=10*10**-9
    #k+=0.5
    z=1000*c
    c+=1
    arr0=getarr(0)
    arr1=getarr(1)
    arr2=getarr(2)
    arr3=getarr(3)
    arrx=[arr0[i]+arr1[i] for i in range(len(arr0))]+[arr2[i]+arr3[i] for i in range(len(arr0))]
    ax2.imshow(arrx, cmap='turbo', interpolation='nearest')
    print(z,c)

animation = FuncAnimation(fig1, update1, frames=range(100), interval=300)
animation2 = FuncAnimation(fig2, update2, frames=range(100), interval=300)

plt.show()