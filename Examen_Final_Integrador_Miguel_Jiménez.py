#Miguel Jiménez Padilla
#19/10/20
#Examen integrador final

def modificar_lista(lista):
    decoy=[]
    
    for i in range(len(lista)):
        if lista[i] not in decoy:
            decoy.append(lista[i])#borrar duplicados

    r=sorted(decoy, reverse=True)#mayor a menor
    
    decoy2=[]
    for p in r:
        if p%2==0:
            decoy2.append(p)#eliminar impares (solamente agrega pares)
    
    decoy3=decoy2[:]
    decoy3=sum(decoy3)#suma
    
    decoy=[]#reciclar variable decoy
    decoy.append(decoy3)#añadir como primer elemento de la lista la suma realizada
    
    
    for q in range(len(decoy2)):
        decoy.append(decoy2[q])
    
    return decoy

def cadenas_y_listas(num):
    
    lista=[]
    for a in range(num):
        work=input()
        lista.append(work)
    
    
    var=''
    count=''
    newlist=[]
    for z in range(len(lista)):
        count=''
        for v in lista[z]:
            if v=='A' or v=='a':
                var='#'
            elif v=='E' or v=='e':
                var='&'
            elif v=='I' or v=='i':
                var='+'
            elif v=='O' or v=='o':
                var='*'
            elif v=='U' or v=='u':
                var='/'
            else:
                var=v
            count=count+var
        newlist.append(count)
        
    print(newlist)
    
    for l in range(len(newlist)):
        print(lista[l],'>>',newlist[l])
    

def main():
    tion=''
    while tion!='0':
        tion=input('\nMenú\n0.Salir\n1.Problema 1\n2.Problema 2\nopción: ')
        
        if tion=='1':
            elementos=int(input('Ingrese la cantidad de elementos de la lista: '))
            if elementos>0:
                lista=[]
                for o in range(elementos):
                    opc=int(input())
                    lista.append(opc)
                    
                x=modificar_lista(lista)
                print(x)
            else:
                print('Lista vacía')
                
        elif tion=='2':
           num=int(input('Ingrese el número de palabras a codificar: '))
           if num>0:
              cadenas_y_listas(num)
main() 