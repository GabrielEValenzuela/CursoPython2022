import random as rd

MAX_ENVIOS = 2**32-1
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

#Añadir mas localidades

def obtenerDatos():
    datos = {}
    for i in range(MAX_ENVIOS):
        datos['cod']        = i
        datos['org']        = LOCALIDADES[rd.randint(0,len(LOCALIDADES))]
        datos['dst']        = LOCALIDADES[rd.randint(0,len(LOCALIDADES))]
        datos['entregado']  = rd.randint(0,1)
    return datos