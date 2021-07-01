#Fibonacci
#Miguel Jiménez



def fibonacci():
    enter=-1
    while enter<0:
        enter=int(input())
    x=0
    y=0
    z=0
    tot=[]
    
    
    for i in range (0,enter):
        if i==0:
            tot.append(x)
        if i==1:
            y=1
            tot.append(y)
        if i==2:
            z=x+y
            tot.append(z)
        elif i>2:
            
            x=y
            y=z
            z=x+y
            tot.append(z)
            
    print(tot)
fibonacci()
            
            
            
        
        