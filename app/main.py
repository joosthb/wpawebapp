from fastapi import FastAPI, Request, Form
from typing import Annotated
from fastapi.templating import Jinja2Templates

from app.wpa_psk import wpa_psk
from app.schemas import *
import app.models
from app.database import Base, engine, SessionLocal

from sqlalchemy.orm import Session
#This will create our database if it doesent already exists
Base.metadata.create_all(engine)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


data = []

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/connection")
def createConnection(connection: Connection):
  #  Inplace replace pass for psk 
   connection.psk = wpa_psk(connection.ssid, connection.psk)
   data.append(connection.dict())
   return data

@app.get("/connection/{id}")
def readConnection(id: int):
   return data[id]

@app.put("/connection/{id}")
def updateConnection(id:int, connection: Connection):
    connection.psk = wpa_psk(connection.ssid, connection.psk)
    data[id] = connection
    return data

@app.delete("/connection/{id}")
def deleteConnection(id: int):
   data.pop(id)
   return data

@app.get("/connections")
def get_connections():
   return data

@app.get("/wpa_supplicant.conf")
def get_wpa_sup(request: Request):
    return templates.TemplateResponse('wpa_supplicant.conf', context={'request': request, 'networks': data})

# @app.get("/form")
# def form_post(request: Request):
#     result = "Type a number"
#     return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

# @app.post("/form")
# async def gen_psk(request: Request, ssid: Annotated[str, Form()], password: Annotated[str, Form()]):
#     result = wpa_psk(ssid, password)
#     return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

