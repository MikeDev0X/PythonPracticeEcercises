#Miguel Jiménez Padilla
#Calcular suma de sodio, proteínas, lípidos, carbohidratos y calorías


def sodio(n):
    
    contador=0
    for i in range (1,n+1):
        numero=float(input())
        contador=contador+numero
    print('\n\nLa cantidad de sodio es: ', contador)
    
    
def proteinas(n):

    contador=0
    for i in range (1,n+1):
        numero=float(input())
        contador=contador+numero
    print('\n\nLa cantidad de proteínas es: ', contador)
    
def lipidos(n):

    contador=0
    for i in range (1,n+1):
        numero=float(input())
        contador=contador+numero
    print('\n\nLa cantidad de lípidos es: ', contador)
    
def carbohidratos(n):

    contador=0
    for i in range (1,n+1):
        numero=float(input())
        contador=contador+numero
    print('\n\nLa cantidad de carbohidratos es: ', contador)

def calorias(n):

    contador=0
    for i in range (1,n+1):
        numero=float(input())
        contador=contador+numero
    print('\n\nLa cantidad de calorías es: ', contador)


def main():

    tion=1
    while tion!=0 :
        try:
            tion=int(input('\n\nElija una de las siguientes opciones: \n 1: sodio \n 2: proteínas \n 3: lípidos \n 4: carbohidratos \n 5: calorías \n 0: salir \n'))
        except:
            print('\n\nERROR, ingrese un caracter válido\n')
        else:
            if tion==1:
                n=int(input('Ingrese la cantidad de iteraciones de sodio: '))
                sodio(n)
            elif tion==2:
                n=int(input('Ingrese la cantidad de iteraciones de proteínas: '))
                proteinas(n)
            elif tion==3:
                n=int(input('Ingrese la cantidad de iteraciones de lípidos: '))
                lipidos(n)    
            elif tion==4:
                n=int(input('Ingrese la cantidad de iteraciones de carbohidratos: '))
                carbohidratos(n)
            elif tion==5:
                n=int(input('Ingrese la cantidad de iteraciones de calorías: '))
                calorias(n)
            elif tion<0 or tion>5:
                print('\n\nEse número no está dentro de las opciones,intente nuevamente')
    
    
main() 
    
    
    
    
