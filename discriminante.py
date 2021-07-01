#Miguel Jiménez Padilla
import math

a=int(input())
b=int(input())
c=int(input())

if a==0 and b==0:
    print('No tiene solucion')
elif a==0 and b!=0:
    print('No tiene solucion')
elif a!=0 and b!=0:
    d=((b**2)-(4*a*c))
    x1=(((-b)+(d)**(1/2))/2*a)
    x2=(((-b)-(d)**(1/2))/2*a)
    x3=(-b/(2*a))
    if d<0:
        print('Raices complejas')
    elif d>0:
        print (x1)
        print (x2)
    else:
        print(x3)
    