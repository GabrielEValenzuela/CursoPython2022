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
    #TizianoQuevedo
    

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
    destinos= barrios['dst']
    DESTINO.append(destinos)

    
#tasas de entregas y no entregas
print("TASAS DE ENTREGA POR BARRIO")
I=0 
while(I<len(d.LOCALIDADES)): 
    for barrios in d.LOCALIDADES: 
        cantidad_de_entregas_y_no_entregas_totales= DESTINO.count(barrios)
        entrega= destino_entregado.count(barrios)
        no_entrega= destino_no_entregado.count(barrios)
        tasa_de_entrega= entrega*100/ cantidad_de_entregas_y_no_entregas_totales
        tasa_de_no_entregados = no_entrega*100 / cantidad_de_entregas_y_no_entregas_totales
        I=I+1

        print ("La tasa de envios entregados de ", barrios , "es de: {:.2f} %" .format(tasa_de_entrega))
        print ("La tasa de envios no entregados de ", barrios , "es de: {:.2f} %" .format(tasa_de_no_entregados))
        
#Mayor cantidad de envios y de recibidos
#ciudades origen
origen=[]
for emisores in d.obtenerDatos():
    ciudades=emisores ['org']
    origen.append(ciudades)

nombre_ciudades=list(set(origen)) #Lo que hago es pasarlo a un conjunto, de forma que solamente tenga las nombres no repetidas
# y la cantidad de ciudades distintas. Luego lo paso a lista para poder leerlos
j=0
envios_por_ciudades=[] #aquí voy a guardar la cantidad de envios que vaya contando por ORDEN de aparicion en la lista anterior
while j<len(nombre_ciudades):
    cantidad_envios_ciudad_j=origen.count(nombre_ciudades[j])
    envios_por_ciudades.append(cantidad_envios_ciudad_j) # almaceno la cantidad de envios de una ciudad en la posicion j
    j=j+1

maximos_envios=nombre_ciudades[envios_por_ciudades.index(max(envios_por_ciudades))] 
#en el bloque anterior, lo que hago es sacar el valor maximo de la lista envios_por_ciudades, luego obtengo la posicion de 
#dicho valor para luego ir a la misma posicion en nombre_ciudades y atribuirle el nombre a la variable maximos_envios
print ('La mayor cantidad de envios se realizan en: ', maximos_envios)
#Intente hacer la maxima de entregas pero nose cual es mi error
maximo_de_entregas=destino_entregado[entrega.index(max(entrega))]
print ("La mayor cantidad de entregas se realiza en: ", maximo_de_entregas)