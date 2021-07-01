import random
def matrix():
    num=0
    while num<5:
        num=int(input('Ingrese el grado de la matriz: \n'))
        
        matrix=[]
        lista=[]
        
        for i in range (num*num):
            lista.append(random.randint(0,100))

        
    letra=' '
    while letra !='E' and letra !='L' and letra !='X':
        letra=input('Ingrese una letra X,E o L: \n')
    
    newlista=[]
    lengt=len(lista)
    count=0
    
    
    
    
    '''if letra=='X':
        
        while count!=lengt:
            if count%2==0:
                newlista.append(lista[count])
            else:
                newlista.append(' ')
            count+=1
        print(newlista)'''
        
        
    newlista=[]
    var1=0
    var2=0
    
    for i in range (num):
            
        for t in range (num):
            if t==0 or t==num:
                print(lista[0],(num-2)*'    ',lista[num])
            elif t!=num//2:
                print('    '*t,lista[t],'    '*t,lista[t],'    '*t)
            else:
                print('    '*t,lista[t],'    '*t)
        
        
        
        
        
        
        
        
        
        '''elif letra=='E':
        print(matrix[0])
        lone=int(len(num))
        lone=round(lone/2)
        for i in range (1,lone):
            print(matrix[i][0])
        print(matrix[lone])
        for i in range (lone,num-1):
            print(matrix[i][0])    
        print(matrix[num])'''
        
        
        
matrix()