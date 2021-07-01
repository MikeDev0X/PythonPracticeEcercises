#Miguel Jiménez Padilla
#Numero al cuadrado mayor que N

def mayor(n):
    x=1
    while n>=x**2:
        x=x+1
    return x
       
r=(mayor(int(input())))
print(r)