#RETO MATRICES
#Equipo:
#Jorge E. Turner Escalante A01423182
#Luis Sebastian Flores Rodriguez A01424653
#Miguel Jimenez Padilla A01423189



from random import randint

def generador(grado):
# Square matrix with random numbers
    return [ [randint(0,100) for c in range(grado)] for r in range(grado)]

def Xmatrix(deg, matriz):
#New Matrix with X shape
    Xmatriz = []
    ndeg = 0
    mark1 = 0
    Xmatriz = matriz
    
    if deg%2 == 1:
        count = deg-1
        for row in range(deg):
            for col in range(deg):
                if row != col and col != count:
                    Xmatriz[col][row] = ""
            count -= 1
            
    
    if deg > 2:
        count = deg-1
        for row in range(deg):
            for col in range(deg):
                if row != col and col != count:
                    Xmatriz[col][row] = ""
            count -= 1
    
    for i in range(deg):
        print(Xmatriz[i])
    return Xmatriz

def Ematrix(deg, matriz):
#New Matrix with E shape
    ndeg = 0
    Ematriz = []
    if deg%2 == 0:
        ndeg = deg/2
        for row in range(deg):
            if row == 0 or row == ndeg or row+1 == deg:
                Ematriz.append(matriz[row])
                print(matriz[row])
            else:
                Ematriz.append(matriz[row][0:1])
                print(matriz[row][0:1])

    else:
        ndeg = (deg-1)/2
        for row in range(deg):
            if row == 0 or row == ndeg or row+1 == deg:
                Ematriz.append(matriz[row])
                print(matriz[row])
            else:
                Ematriz.append(matriz[row][0:1])
                print(matriz[row][0:1])
    return Ematriz

def Lmatrix(deg, matriz):
#New Matrix with L shape
    Lmatriz = []
    for row in range(deg):
        if row+1 != deg:
            Lmatriz.append(matriz[row:row+1][0:1])
            print(matriz[row][0:1])
        else:
            Lmatriz.append(matriz[-1])
            print(matriz[-1])
    return Lmatriz

def main():
    while True:
        try:
            deg = int(input("Grado de matriz (mayor a 1): "))
        except:
            print("No es un número")
        else:
            if deg > 1:
                matriz = generador(deg)
                break
            else:
                print("Grado inválido")
                continue
    while True:
        try:
            letra = input('Ingresa una letra "X", "E", "L": ')
        except:
            continue
        else:
            if letra == "X":
                print()
                Xmatrix(deg, matriz)
                break
            elif letra == "E":
                print()
                Ematrix(deg, matriz)
                break
            elif letra == "L":
                print()
                Lmatrix(deg, matriz)
                break
            else:
                print("No es una letra válida")
                continue
main()
                