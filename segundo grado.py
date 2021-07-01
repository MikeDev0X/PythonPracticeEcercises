#Miguel Jiménez Padilla
import math

a=int(input())
b=int(input())
c=int(input())


def di():
    #calcula discriminante
    d=((b**2)-(4*a*c))
    return(d)

if a==0 and b==0:
    print('No tiene solucion')
elif a==0 and b!=0:
    print('No tiene solucion')
elif a!=0 and b!=0:
    
    x1=(((-b)+(di())**(1/2))/2*a)
    x2=(((-b)-(di())**(1/2))/2*a)
    x3=(-b/(2*a))
    if di()<0:
        print('Raices complejas')
    elif di()>0:
        print (x1)
        print (x2)
    else:
        print(x3)