#Miguel Jiménez Padilla
#combina listas

def listas():
    n1=int(input())
    n2=int(input())
    lista1=[]
    lista2=[]
    listaF=[]
    countA=0
    countB=0
    
    
    if n1<=0 or n2<=0:
        print('Error')
    else:
        print('-----')
        
        for i in range (0,n1):
            x1=input()
            lista1.append(x1)
            countA+=1
        
        print('-----')
        
        for i in range (0,n2):
            x2=input()
            lista2.append(x2)
            countB+=1
            
        if countA>countB:
            for i in range (0,countB):
                listaF.append(lista1[i]) 
                listaF.append(lista2[i])
            for i in range (countB,countA):
                listaF.append(lista1[i])
                
        elif countB>countA:
            for i in range (0,countA):
                listaF.append(lista1[i]) 
                listaF.append(lista2[i])
            for i in range (countA,countB):
                listaF.append(lista2[i])
                     
        else:
            for i in range (0,countA):
                listaF.append(lista1[i]) 
                listaF.append(lista2[i])
                
        
        print('-----')
        print(lista1)
        print(lista2)
        print(listaF)
        


listas()


