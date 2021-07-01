#Miguel Jiménez Padilla
#Mezcla y ordena listas


def mezcla():
    enter=''
    lista=[]
    newlist=[]
    junta=[]
    countA=0
    countB=0
    countF=0

    while enter!= '*':
        enter=input()
        if enter!='*':
            lista.append(int(enter))
            countA+=1
        else:
            break
    
    enter=''
    
    while enter!= '*':
        enter=input()
        if enter!='*':
            newlist.append(int(enter))
            countB+=1
        else:
            break    
        
    
    countF=countA+countB
    
    for i in range (0,countA):
        junta.append(lista[i])
    for i in range (0,countB):
        junta.append(newlist[i])
        
        
    
    junta.sort()
    
    
    print('L1=')
    print(lista)
    print('L2=')
    print(newlist)
    print('LORDENADA=')
    print(junta)
    
mezcla()

