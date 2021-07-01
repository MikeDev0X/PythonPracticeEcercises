#Miguel Jiménez Padilla, Gabdiel Adame

multiplicador=int(input())
multiplicando=int(input())

suma=0
s=0
if multiplicador>=0 and multiplicando>=0:
    print(multiplicador, multiplicando)
    
    while multiplicador>1:
        if multiplicador%2==0:
            multiplicador=((multiplicador)//2)
            multiplicando=(multiplicando*2)
            print(multiplicador, multiplicando )
        else:
            s=multiplicando+s
            multiplicador=((multiplicador)//2)
            multiplicando=(multiplicando*2)
            
            
            print(multiplicador, multiplicando )
            
suma=multiplicando+suma+s
print("Resultado=" + str(suma))