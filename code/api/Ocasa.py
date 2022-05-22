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

    #Clasificacion de entregas
def clasificarEntregas(listEnvios):
    """
       Clasificacion de Entregas
       Params
       ------
       dicEntregas, conditional
       Diccionario con los datos de las entregas
    """
    dicEntregas   = {}
    for envio in listEnvios:
        if envio.obtenerDestino() not in dicEntregas:
            dicEntregas[envio.obtenerDestino()] = {"entregados": 0, "no_entregados": 0}
        if envio.estadoEntrega():
            if envio.obtenerDestino() in dicEntregas:
                dicEntregas[envio.obtenerDestino()]["entregados"] += 1
        else:
            if envio.obtenerDestino() in dicEntregas:
                dicEntregas[envio.obtenerDestino()]["no_entregados"] += 1
    return dicEntregas

def calcularTasaEntregas(dicEntregas):
    """
        Tasa de entregas 
        Params
        ------
        dicEntregas, porcentaje 
        Diccionario con las tasas de entrega para cada barrio 
    """
    for envio in dicEntregas:
        tasaEntrega = dicEntregas[envio]["entregados"]/(dicEntregas[envio]["entregados"]+dicEntregas[envio]["no_entregados"])
        print("La tasa de entrega para el barrio {0} es del {1:.2f}".format(envio,(tasaEntrega)))

def maxEnviosEntregados(dicEntregas):
    """
        @ToDo Documentar
    """
    maximo=-1
    localidad=''
    for envios in dicEntregas:
        if dicEntregas[envios]['entregados']>maximo:
            maximo=dicEntregas[envios]['entregados']
            localidad=envios
    return localidad,maximo

def maxEnviosNoEntregados(dicEntregas):
    """
        @ToDo Documentar
    """
    maximo=-1
    localidad=''
    for envios in dicEntregas:
        if dicEntregas[envios]['no_entregados']>maximo:
            maximo=dicEntregas[envios]['no_entregados']
            localidad=envios
    return localidad,maximo