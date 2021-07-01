#Miguel Jiménez Padilla
import math

r=float(input())
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())

d=math.sqrt((x2-x1)**2+(y2-y1)**2)

if d>r:
    print('FUERA')
elif d<r:
    print('DENTRO')
else:
    print('SOBRE')







