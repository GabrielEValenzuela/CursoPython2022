#Programa principal

#Autores:
    #gabrielv
    #nahuelalt
    #tomasrearte
    #franferr02
    #francovega
    #lucksJa
    #RoBengio
    #MateoQuispe
    

#Descomentar para probar
import random
from re import I 
import data as d
#print(d.obtenerDatos())

#generador de codigo de seguimiento 
longitud = 8
valores = "0123456789"
aux = ""
for codigo in d.obtenerDatos():
    longitud = 8
    valores = "0123456789"
    aux = ""
    aux = aux.join([random.choice(valores) for i in range(longitud)])
    codigo ['cod']= "OC" + aux
  
#Clasificacion de entregas
destino_entregado=[]
destino_no_entregado=[]
for fichas_de_envio in d.obtenerDatos()  :
    if fichas_de_envio ['entregado'] == 1 : 
        destino_entregado.append( fichas_de_envio ['dst'])
    else:
        destino_no_entregado.append( fichas_de_envio ['dst'])
# print (destino_entregado)
# print (destino_no_entregado)

# lista de destinos
DESTINO=[]
for barrios in d.obtenerDatos():
    destinos= d.obtenerDatos['dst']
    DESTINO.extend(destinos['dst'])

I=0 
while(I<len(d.LOCALIDADES)): 
    for barrios in d.LOCALIDADES: 
        cantidad_de_entregas_total=

