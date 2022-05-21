from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Mi primer": "APIRest"}

@app.get("/v1")
def v1():
    return {"Version": "V1"}

@app.get("/saludar/{nombre}")
def saludar_por_nombre(nombre: str):
    return {"Hola": nombre}