#Miguel Jiménez

s=str(input())
c=str(input())
t=int(input())

def silla(s):
    if s=='B':
        return (700)
    elif s=='E':
        return (900)
    elif s=='L':
        return (1500)

def cantidad(t,s):
    
    silla(s)
    mult=(t*s)
    return(mult)
    


def desc(c):
    cantidad(t,s)
    
    if c=='N':
        if mult>=10000 and mult<=20000:
            pdescuento=(mult*0.1)
            return (pdescuento)
        elif mult>=20000:
            pdescuento=(mult*0.2)
            return (pdescuento)
    elif c=='R':
        pdescuento=(mult*0.2)
        return (pdescuento)
        
def final():
    silla(s)
    cantidad(t,s)
    desc(c,t,s)
    
    
    print(mult)
    print(pdescuento)
    print(mult-(pdescuento))
            
final()


