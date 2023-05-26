
import numpy as np
import random
import math


def fxy(x1, x2):
    return (x1**2 + x2**2)

def dist(x1,y1,x2,y2):
    a = (x1-x2)**2+(y1-y2)**2
    a = np.sqrt(a)
    return a

w= 0.5
c1= 2
c2= 2
r1=(bool(random.getrandbits(1))) * random.random()*1
r2=(bool(random.getrandbits(1))) * random.random()*1

print(r1,r2)


px = np.array([np.array([(-1)** (bool(random.getrandbits(1))) * random.random()*10]) for _ in range(15)])
py = np.array([np.array([(-1)** (bool(random.getrandbits(1))) * random.random()*10]) for _ in range(15)])

vx = np.array([np.array([(-1)** (bool(random.getrandbits(1))) * random.random()*10]) for _ in range(15)])
vy = np.array([np.array([(-1)** (bool(random.getrandbits(1))) * random.random()*10]) for _ in range(15)])



gbx = 100000
gby = 100000

gb = 1000000000.0

for i in range(15):
    f = fxy(px[i],py[i]) #fitness value
    if f < gb:
        gbx = px[i]
        gby = py[i]
        gb = f

xb = px
yb = py


for i in range(5000):
    
    for i in range(15):
        
        #t1 = c1*r1*dist(xb[i],yb[i],px[i],py[i])
        #t2 = c2*r2*dist(gbx,gby,px[i],py[i])
        #t1 = c1*r1*(xb[i]-px[i])
        #vx[i] = w*vx[i]+t1+t2
        #vy[i] = w*vy[i]+t1+t2
        
        vx[i] = w*vx[i]+c1*r1*(xb[i]-px[i])+c2*r2*(gbx-px[i])
        vy[i] = w*vy[i]+c1*r1*(yb[i]-py[i])+c2*r2*(gby-py[i])
        
        if(vx[i]<-3.0):
            vx[i]=-3.0
        if(vx[i]>3.0):
            vx[i]=3.0
            
        if(vy[i]<-3.0):
            vy[i]=-3.0
        if(vy[i]>3.0):
            vy[i]=3.0
            
    for i in range(15): #update current position
        px[i]=px[i]+vx[i]
        py[i]=py[i]+vy[i]
    
    for i in range(15):
        f  = fxy(px[i], py[i])
        if f<fxy(xb[i], yb[i]):
            xb[i]=px[i]
            yb[i]=py[i]
        if(f<gb):
            gb = f
            gbx = px[i]
            gby = py[i]
            
            

print(gb)
        





