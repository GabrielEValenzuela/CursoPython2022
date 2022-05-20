import data as d
import random as rd

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
def generarUUID(dicEnvios):
    """
        Generar IDs únicos para los envios

        Params
        ------
        dicEnvios, dict, require
        Diccionario con todos los envíos
    """
    MAX_LONG = 8
    valores  = "0123456789"
    for codigo in dicEnvios:
        codigo['cod'] = "OC" + ''.join([rd.choice(valores) for i in range(MAX_LONG)])
  
#Clasificacion de entregas
def clasificarEntregas(dicEnvios):
    """
       Clasificacion de Entregas
       Params
       ------
       dicEntregas, conditional
       Diccionario con los datos de las entregas
    """
    dicEntregas   = {}
    for envio in dicEnvios:
        if envio['dst'] not in dicEntregas:
            dicEntregas[envio['dst']] = {"entregados": 0, "no_entregados": 0}
        if envio['entregado']:
            if envio['dst'] in dicEntregas:
                dicEntregas[envio['dst']]["entregados"] += 1
        else:
            if envio['dst'] in dicEntregas:
                dicEntregas[envio['dst']]["no_entregados"] += 1
    return dicEntregas

def calcularTasaEntregas(dicEntregas):
    """
        @ToDo Documentar
    """
    for envio in dicEntregas:
        tasaEntrega = dicEntregas[envio]["entregados"]/(dicEntregas[envio]["entregados"]+dicEntregas[envio]["no_entregados"])
        print("La tasa de entrega para el barrio {0} es del {1:.2f}".format(envio,(tasaEntrega)))

#Mayor cantidad de envios y de recibidos
#ciudades origen
def maxEnvios(dicEnvios):
    """
        @ToDo Documentar
    """
    #origen=[]
    #for emisores in d.obtenerDatos():  
    #ciudades=emisores ['org']
    #origen.append(ciudades)
    #nombre_ciudades=list(set(origen)) #Lo que hago es pasarlo a un conjunto, de forma que solamente tenga las nombres no repetidas
    # y la cantidad de ciudades distintas. Luego lo paso a lista para poder leerlos
    #j=0
    #envios_por_ciudades=[] #aquí voy a guardar la cantidad de envios que vaya contando por ORDEN de aparicion en la lista anterior
    #while j<len(nombre_ciudades):
        #cantidad_envios_ciudad_j=origen.count(nombre_ciudades[j])
        #envios_por_ciudades.append(cantidad_envios_ciudad_j) # almaceno la cantidad de envios de una ciudad en la posicion j
        #j=j+1

    #maximos_envios=nombre_ciudades[envios_por_ciudades.index(max(envios_por_ciudades))] 
    #en el bloque anterior, lo que hago es sacar el valor maximo de la lista envios_por_ciudades, luego obtengo la posicion de 
    #dicho valor para luego ir a la misma posicion en nombre_ciudades y atribuirle el nombre a la variable maximos_envios
    #print ('La mayor cantidad de envios se realizan en: ', maximos_envios)
    #Intente hacer la maxima de entregas pero nose cual es mi error
    #maximo_de_entregas=destino_entregado[entrega.index(max(entrega))]
    #print ("La mayor cantidad de entregas se realiza en: ", maximo_de_entregas)
    pass

def main():
    datos = d.obtenerDatos()
    print('Datos:')
    generarUUID(datos)
    print(datos)
    print('Funcion de clasificar')
    entregas = clasificarEntregas(datos)
    print(entregas)

if __name__ == "__main__":
    main()