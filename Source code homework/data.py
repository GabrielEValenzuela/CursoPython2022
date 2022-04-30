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

#Añadir mas localidades para la próxima clase

def obtenerDatos():
    datos = []
    for i in range(MAX_ENVIOS):
        dato = {}
        dato['cod']        = i
        dato['org']        = LOCALIDADES[rd.randint(0,len(LOCALIDADES))]
        dato['dst']        = LOCALIDADES[rd.randint(0,len(LOCALIDADES))]
        dato['entregado']  = rd.randint(0,1)
        datos.append(dato)
    return datos