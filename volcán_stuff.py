#función para sacar velocidades

import math
import random

intervalos=12
masa=800
#masa=random.randint(600,1000)
n=2
k=2

def velocity(velocity,angle):
    v0y=velocity*math.sin(math.radians(angle))
    v0x=velocity*math.cos(math.radians(angle))
        
    listv=[]
    listv.append(v0x)
    listv.append(v0y)
    
    return listv



vxvy=velocity(40,30)
#print(vxvy)

def tiempo_vuelo(vxvy):
    tiempo_vuelo=(vxvy[1]/9.81)*2
    
    
    return tiempo_vuelo

tiempo_vuelo=tiempo_vuelo(vxvy)
paso_t=tiempo_vuelo/intervalos

def posicion_x(vxvy,intervalos):########################
    
    posx=[]
    x=0
    for i in range(0,intervalos):
        x=(i*vxvy[0])/2 #index 0 of list equals x
        posx.append(x)
        x=0
    
    return posx


posx=posicion_x(vxvy,intervalos)
#print(posx)    


def baldirri(k,n,masa,intervalos,vxvy,tiempo_vuelo):
    velocidadesxy=vxvy[:]
    velist=[]
    acclist=[]
    while intervalos:
        aF = (k * velocidadesxy[1] **n)/masa
        velocidadesxy[1] = velocidadesxy[1] - (9.81 + aF) * paso_t
        intervalos -= 1
        velist.append(velocidadesxy[1])
        acclist.append(aF)
    
    return velist, acclist
    
baldirri=baldirri(k,n,masa,intervalos,vxvy,tiempo_vuelo)#baldirri[0]= velocidades, baldirri[1]=aF
    
def pos_y(vxvy,baldirri):
    #v0y*t-((9.81-AF)*t**2)/2)    
    listay=[0]
    #listay.append(vxvy[1])
    Yk=0
    for emma in range(1,intervalos):
        Yk=(vxvy[1]*emma-(0.5*(9.81-baldirri[1][emma])*(emma)**2))/2
        listay.append(Yk)
    return listay
    
posy=pos_y(vxvy,baldirri)
    
    
    
def juntar(posx,posy):
    TOT=[]
    matrix=[]
    for l in range(intervalos):
        TOT=[]
        TOT.append(posx[l])
        TOT.append(posy[l])
        matrix.append(TOT)

    return matrix
juntar=juntar(posx,posy)
print(juntar)
