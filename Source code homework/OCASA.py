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
        Tasa de entregas 
        Params
        ------
        dicEntregas, porcentaje 
        Diccionario con las tasas de entrega para cada barrio 
    """
    for envio in dicEntregas:
        tasaEntrega = dicEntregas[envio]["entregados"]/(dicEntregas[envio]["entregados"]+dicEntregas[envio]["no_entregados"])
        print("La tasa de entrega para el barrio {0} es del {1:.2f}".format(envio,(tasaEntrega)))

#Mayor cantidad de envios y de recibidos
#ciudades origen
def maxEnvios(dicEntregas):
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

def maxEnviosNoentregados(dicEntregas):
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


def main():
    datos = d.obtenerDatos()
    print('Datos:')
    generarUUID(datos)
    print(datos)
    print('Funcion de clasificar')
    entregas = clasificarEntregas(datos)
    print(entregas)
    print('La localidad con maximos envios entregados es: ',maxEnvios(entregas))
    print('La localidad con maximos envios no entregados es: ',maxEnviosNoentregados(entregas))


def ObtenerEnvios(Codigo_envios,lista_de_envios):
    for envios in lista_de_envios:
        if Codigo_envios==envios['cod']:
            return envios







if __name__ == "__main__":
    main()

