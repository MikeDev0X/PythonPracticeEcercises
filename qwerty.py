cadena = input()
guion = int(input())
total = len(cadena)
contador = 0
contador2 = 0

if guion <= 0:
    print ("Error")
elif total == guion:
    print(cadena)
else:
    for i in range(0,total, guion):
        contador = contador + guion
        print(cadena[contador2:contador], end="")
        if contador2 + guion < total:
            print("-", end="")
        contador2 = contador2 + guion