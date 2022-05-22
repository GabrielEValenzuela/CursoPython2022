import random as rd
import code.api.Envio as e

MAX_ENVIOS = 2**8-1 #Descomentar y comentar el siguiente para produccion
#MAX_ENVIOS = 2**32-1
LOCALIDADES = [
    "Barrio Alberdi",
    "Barrio Bajada San Roque",
    "Barrio Bella Vista",
    "Barrio Centro",
    "Barrio Cupani",
    "Barrio Cáceres",
    "Barrio Ducasse",
    "Barrio Güemes",
    "Barrio Maurizi",
    "Barrio Nueva Córdoba",
    "Barrio Observatorio",
    "Barrio Parque Sarmiento",
    "Barrio Paso de los Andes",
    "Barrio Providencia",
    "Barrio Quinta Santa Ana",
    "Barrio Rogelio Martinez",
    "Retiro, San Nicolás",
    "Puerto Madero",
    "San Telmo",
    "Montserrat",
    "Constitución",
    "Villa Real",
    "Monte Castro",
    "Versalles",
    "Floresta",
    "Vélez Sarsfield",
    "Villa Luro"
]

#Añadir mas localidades para la próxima clase

def obtenerDatos() -> list:
    datos = []
    for i in range(MAX_ENVIOS):
        dato = e.Envio(generarTrackCode(),LOCALIDADES[rd.randint(0,len(LOCALIDADES)-1)],LOCALIDADES[rd.randint(0,len(LOCALIDADES)-1)])
        if rd.randint(0,1):
            dato.envioEntregado()
        datos.append(dato)
    return datos

def generarTrackCode():
    """
        Generar IDs únicos para los envios

        Params
        ------
        dicEnvios, dict, require
        Diccionario con todos los envíos
    """
    return str('OC12345')