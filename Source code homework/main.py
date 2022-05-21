from pydantic import BaseModel
from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def read_root():
    return "Bienvenido a sistema OCASA... Tus entregas fallidas aseguradas"


@app.get("/envio/{codigo_envio}")
def obtener_por_id(item_id: str):
    pass

@app.get("/envios")
def obtener_todos():
    pass
