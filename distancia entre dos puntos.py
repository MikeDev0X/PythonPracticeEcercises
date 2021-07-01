#Miguel Jiménez Padilla
#Desarrolla un programa en Python que calcule la distancia entre dos puntos del plano cartesiano.
import math 

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

c=math.sqrt(((x2-x1)**(2)+(y2-y1)**(2)))


print("distancia={0:.2f}".format(c))

