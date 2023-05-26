
import numpy as np
import random
import math

l_or = [0,1,1,1]
l_and = [0,1,1,1]
fx = [0,0,1,1]
fy = [0,1,0,1]


def dist2(x, y):
    return abs(y-x)

def fxy_or(x1, x2, x3):
    
    
    return dist2(10,x1)+dist2(10, x2)+ dist2(-5, x3)
    
    #f_or = 1
    
    #if(x3<0 and x1>=0 and x2>=0 and abs(x3)<min(x1, x2) ):
    #    f_or=1
    #else :
    #    f_or=0
    
   # return f_or



    #f_and = 1
    
    
    
    #for i in range(4):
    #    out = x1*fx[i]+x2*fy[i]+x3
        
    
    
def fxy_and(x1, x2, x3):
    
    f_and = 1
    
    if(x3<0 and x1>=0 and x2>=0 and abs(x3)>x1 and abs(x3)>x2 and abs(x3)<x1+x2 ):
        f_and=1
    else :
        f_and=0
    
    return f_and   
    

def dist(x1,y1,x2,y2):
    a = (x1-x2)**2+(y1-y2)**2
    a = np.sqrt(a)
    return a

w= 0.6
c1= 2
c2=2
r1=(bool(random.getrandbits(1))) * random.random()*1
r2=(bool(random.getrandbits(1))) * random.random()*1

print(r1,r2)


px = np.array([np.array([(-1)** (bool(random.getrandbits(1))) * random.random()*10]) for _ in range(5)])
py = np.array([np.array([(-1)** (bool(random.getrandbits(1))) * random.random()*10]) for _ in range(5)])
pz = np.array([np.array([(-1)** (bool(random.getrandbits(1))) * random.random()*10]) for _ in range(5)])

vx = np.array([np.array([(-1)** (bool(random.getrandbits(1))) * random.random()*10]) for _ in range(5)])
vy = np.array([np.array([(-1)** (bool(random.getrandbits(1))) * random.random()*10]) for _ in range(5)])
vz = np.array([np.array([(-1)** (bool(random.getrandbits(1))) * random.random()*10]) for _ in range(5)])
print(px)
print(py)
print(pz)

print(vx)
print(vy)
print(vz)

gbx = 1000
gby = 1000
gbz = 1000

gb = 100000000.0

for i in range(5):
    f = fxy_or(px[i],py[i], pz[i])
    if f < gb  and px[i]>0 and py[i]>0 and pz[i]<0:
        gbx = px[i]
        gby = py[i]
        gbz = pz[i]
        gb = f

xb = px
yb = py
zb = py


for k in range(5000):
    
    
    for i in range(5):
        
        #t1 = c1*r1*dist(xb[i],yb[i],px[i],py[i])
        #t2 = c2*r2*dist(gbx,gby,px[i],py[i])
        
        vx[i] = w*vx[i]+c1*r1*(xb[i]-px[i])+c2*r2*(gbx-px[i])
        vy[i] = w*vy[i]+c1*r1*(yb[i]-py[i])+c2*r2*(gby-py[i])
        vz[i] = w*vz[i]+c1*r1*(zb[i]-pz[i])+c2*r2*(gbz-pz[i])
        
        if(vx[i]<-3.0):
            vx[i]=-3.0
        if(vx[i]>3.0):
            vx[i]=3.0
            
        if(vy[i]<-3.0):
            vy[i]=-3.0
        if(vy[i]>3.0):
            vy[i]=3.0
        
        if(vz[i]<-3.0):
            vz[i]=-3.0
        if(vz[i]>3.0):
            vz[i]=3.0
    for i in range(5):
        px[i]=px[i]+vx[i]
        py[i]=py[i]+vy[i]
        pz[i]=pz[i]+vz[i]
    
    for i in range(5):
        f  = fxy_or(px[i], py[i], pz[i])
        if f< fxy_or(xb[i], yb[i], zb[i]) and xb[i]>0 and yb[i]>0 and zb[i]<0:
            xb[i]=px[i]
            yb[i]=py[i]
            zb[i]=pz[i]
        if(f< gb  and px[i]>0 and py[i]>0 and pz[i]<0):
            gb = f
            gbx = px[i]
            gby = py[i]
            gbz = pz[i]
     
    if(k<20):
        print(k)
        for i in range(5):
            print(str(px[i])+" " +str(py[i])+" "+str(pz[i]))
        
        print("gbest: ")
        print(gbx, gby, gbz)
        print("")
        print("")
    
    
    
            
            

print(gb)


print(gbx, gby, gbz)

       






