#Miguel Jiménez Padilla
import math

r=float(input())
h=float(input())


def area_cilindro(r,h):
    a=((2*(math.pi)*r*h)+2*((math.pi)*r**2))
    print('area={0:.2f}'.format(a))
    
def volumen_cilindro(r,h):
    v=((math.pi)*r**2*h)
    print('volumen={0:.2f}'.format(v))
    
    
    
    

area_cilindro(r,h)
volumen_cilindro(r,h)



