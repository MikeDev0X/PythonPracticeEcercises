#Miguel Jiménez Padilla
#Realiza un programa que muestre el mayor de 3 números enteros x, y, z proporcionados por el usuario.
#No utilices la función incorporada de Python max ().

a=int(input())
b=int(input())
c=int(input())

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print (b)
elif c>a and c>b:
    print (c)
    