from pydantic import BaseModel
import code.api.Data as d
import code.api.Envio as e
import code.api.Ocasa
from fastapi import FastAPI, HTTPException


app = FastAPI()
database = None

class BodyEnvio(BaseModel):
    cod: str
    org: str
    dst: str

@app.get("/")
def read_root():
    return "Bienvenido a sistema OCASA... Tus entregas fallidas aseguradas"

@app.get("/generate")
def generar_database():
    global database #No es lo mejor usar global, pero necesitamos referenciar la variable fuera de la función :(
    if database == None:
        database = d.obtenerDatos()
        return "A random database has been generated"
    else:
        database += d.obtenerDatos()
        return "A random database has been added"

@app.post("/agregar-envio", status_code=201)
def nuevo_envio(envio: BodyEnvio):
    if envio.cod != "":
        database.append(
            e.Envio(
                track_code=envio.cod,
                org=envio.org,
                dst=envio.dst,
            )
        )
        return envio
    else:
        raise HTTPException(status_code=400, detail="Bad request")


@app.get("/envio/{codigo_envio}")
def obtener_por_id(codigo_envio: str):
    for envio in database:
        if codigo_envio == envio.obtenerCodigo():
            print(envio)
            return envio.obtenerInformacion()
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/envios")
def obtener_todos():
    return database

@app.patch("/envio/{codigo_envio}/success", status_code=201)
def entregar_envio(codigo_envio: str):
    for envio in database:
        if codigo_envio == envio.obtenerCodigo():
            envio.envioEntregado()
            return envio.obtenerInformacion()
    raise HTTPException(status_code=400, detail="Bad request")

@app.patch("/envio/{codigo_envio}/fail", status_code=201)
def entregar_envio(codigo_envio: str):
    for envio in database:
        if codigo_envio == envio.obtenerCodigo():
            envio.envioNoEntregado()
            return envio.obtenerInformacion()
    raise HTTPException(status_code=400, detail="Bad request")

@app.get("/statics")
def estadisticas():
    return {
        "entregas_clasificadas": code.api.Ocasa.clasificarEntregas(database),
        "tasa_entregas": "ToDo",
        "max_entregas": "ToDo",
        "max_fallas": "ToDo"
    }