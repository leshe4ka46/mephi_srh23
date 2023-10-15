import math
import cmath
from scipy.special import jv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
r=39
a=0.25
z=8
E0=5
k=0.05
lambd=1000*10**-9
#centers=[[r/2,r/2],[r/2,-r/2],[-r/2,r/2],[-r/2,-r/2]]
centers=[[r/2,-r/2],[r/2,r/2],[-r/2,-r/2],[-r/2,r/2]]
def getc(x,y):
    return math.exp((k*((x*z)**2+(y*z)**2))/(2*z))/(lambd*z)


# def e(x,y,id):
#     val=math.sqrt(x**2+y**2)
#     return math.pi*a*a*getc(x,y)*E0*abs(complex(-k*(x*centers[id][0]+y*centers[id][1])))*2*jv(2, k*a*math.sqrt(x**2+y**2))/(val if val else 1)



def e(x,y,id):
    val=math.sqrt(x**2+y**2)
    return math.pi*a*a*getc(x,y)*E0*math.exp(-k*(x*centers[id][0]+y*centers[id][1]))*2*jv(2, k*a*(val if val!=0 else 0.08))/(val if val!=0 else 1)

def getarr(id):
    return [[e(i/1000,j/1000,id) for j in range (-40,41)] for i in range(40,-41,-1)]
fig, ax = plt.subplots(nrows=2, ncols=2)
fig2, ax2 = plt.subplots(nrows=1, ncols=1)

arr0=getarr(0)
arr1=getarr(1)
arr2=getarr(2)
arr3=getarr(3)
arrx=[arr0[i]+arr1[i] for i in range(len(arr0))]+[arr2[i]+arr3[i] for i in range(len(arr0))]
ax2.imshow(arrx, cmap='turbo', interpolation='nearest')

def update(frame):
    global k
    k+=0.05
    arr0=getarr(0)
    arr1=getarr(1)
    arr2=getarr(2)
    arr3=getarr(3)
    arrx=[arr0[i]+arr1[i] for i in range(len(arr0))]+[arr2[i]+arr3[i] for i in range(len(arr0))]
    ax2.imshow(arrx, cmap='turbo', interpolation='nearest')
    print(k)


animation = FuncAnimation(fig2, update, frames=range(100), interval=200)



c=0
for row in ax:
    for col in row:
        col.imshow(arr0 if c==0 else arr1 if c==1 else arr2 if c==2 else arr3, cmap='turbo', interpolation='nearest')
        c+=1

plt.show()