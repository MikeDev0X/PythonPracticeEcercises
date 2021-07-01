#Miguel Jiménez Padilla

import math

a=float(input())
b=float(input())
c=float(input())

s=((a+b+c)/2)

t=math.sqrt(s*(s-a)*(s-b)*(s-c))

print("{0:.3f}".format(t))