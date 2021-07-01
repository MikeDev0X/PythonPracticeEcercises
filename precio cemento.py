#Miguel Jimènez Padilla
# 13/08/2020
# Haz un programa sirva para calcular el precio que va a pagar un cliente por comprar cemento.
# El programa debe leer la cantidad de bultos de cemento que va a comprar el cliente, y el precio del bulto de cemento.
# El programa debe mostrar como salida 3 datos uno en cada renglón: el precio antes de impuestos, los impuestos (que son el 16% del precio) y el total a pagar por el cliente.



c=int(input())
p=int(input())

iva=0.16
pInicial=p*c



print(pInicial)
print(pInicial*iva)
print(pInicial*1.16)