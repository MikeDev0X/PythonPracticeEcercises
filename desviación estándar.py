#Miguel Jiménez Padilla
import math

a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())

M=((a+b+c+d+e)/5)

a=(math.fabs(a-M)**2)
b=(math.fabs(b-M)**2)
c=(math.fabs(c-M)**2)
d=(math.fabs(d-M)**2)
e=(math.fabs(e-M)**2)

E=(a+b+c+d+e)

f=math.sqrt(E/5)

print(f)

