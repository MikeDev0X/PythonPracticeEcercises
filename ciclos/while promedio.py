#Miguel Jiménez

def tecla():
    i=0
    contador=0
    suma=0
    while i>=0:
        i=int(input('tecla: \n'))
        if i<0:
            break
        else:
            suma=0
            suma=suma+i
            contador+=suma
        if contador!=0:
            print('El promedio es: ',(suma)/(contador))    

tecla()

    








