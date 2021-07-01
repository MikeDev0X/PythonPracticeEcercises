#Miguel Jiménez Padilla
#Examen
#print("{0:.2f}".format(cals)


def convierte_C_a_K(Centi,it,increm):
    print('#        Centígrados        Kelvin')
    print('_        ___________        ______')
    print()
    for it in range(1,it+1):
        Kelvin=273.15
        Kelvin=Centi+Kelvin
        print(it,'           ', Centi,'           ',"{0:.3f}".format(Kelvin))
        Centi=Centi+increm
        
def media_armonica():
    
    tion=1
    cont=0
    nn=0
    media=0
    while tion!=0:
        
        num=float(input('Ingrese un número positivo, ingrese 0 para salir: \n'))
        
        if num>0:
            cont=cont+1
            nn=nn+(1/num)
            media=((cont)/nn)
            
        elif num==0:
            tion=0
            mediaN=0
            
    
    return(media+mediaN)
    
def main():
    option=1
    while option!=0:
        try:
            option=int(input('\nExamen Miguel \n10/sep/2020 \nMenú \n0.Salir \n1.Convertir grados Centígrados a Kelvin \n2.Calcular la media armónica\n '))
        except:
            print('caracter incorrecto')
        else:
            if option==1:
                Centi=float(input('Ingrese el valor inicial de centigrados a convertir: \n'))
                it=int(input('Ingrese el número de veces que se convertirán los centígrados a kelvin: \n'))
                increm=float(input('Ingrese el incremento entre los valores centígrados: \n'))
                convierte_C_a_K(Centi,it,increm)
            elif option==2:
                print('\nLa media armónica es: ',media_armonica(),'\n')
            elif option<0 or option>2:
                print('Esa opción no está en el menú, intente nuevamente')
            elif option==0:
                print('Adiós\n')
        
main()
