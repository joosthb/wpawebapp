from fastapi import FastAPI, Request, Depends, Form
from typing import Annotated
from fastapi.templating import Jinja2Templates

from app.wpa_psk import wpa_psk
from app import models, schemas
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

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/connection")
def createConnection(connection: schemas.Connection, session = Depends(get_session)):
    itemObject = models.Connection(ssid = connection.ssid, psk = wpa_psk(connection.ssid, connection.psk))
    session.add(itemObject)
    session.commit()
    session.refresh(itemObject)
    return itemObject

@app.get("/connection/{id}")
def readConnection(id:int, session: Session = Depends(get_session)):
    connection = session.query(models.Connection).get(id)
    return connection

@app.put("/connection/{id}")
def updateConnection(id:int, connection:schemas.Connection, session = Depends(get_session)):
    itemObject = session.query(models.Connection).get(id)
    itemObject.ssid = connection.ssid
    itemObject.psk = wpa_psk(connection.ssid, connection.psk)
    session.commit()
    return itemObject

# @app.delete("/connection/{id}")
# def deleteConnection(id: int):
#    data.pop(id)
#    return data

@app.delete("/connection/{id}")
def deleteItem(id:int, session = Depends(get_session)):
    itemObject = session.query(models.Connection).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item was deleted'

@app.get("/connections")
def getConnections(session: Session = Depends(get_session)):
    connections = session.query(models.Connection).all()
    return connections

# @app.get("/wpa_supplicant.conf")
# def get_wpa_sup(request: Request):
#     return templates.TemplateResponse('wpa_supplicant.conf', context={'request': request, 'networks': data})

@app.get("/wpa_supplicant.conf")
def get_wpa_sup(request: Request, session: Session = Depends(get_session)):
    connections = session.query(models.Connection).all()
    return templates.TemplateResponse('wpa_supplicant.conf', context={'request': request, 'networks': connections})

# @app.get("/form")
# def form_post(request: Request):
#     result = "Type a number"
#     return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

# @app.post("/form")
# async def gen_psk(request: Request, ssid: Annotated[str, Form()], password: Annotated[str, Form()]):
#     result = wpa_psk(ssid, password)
#     return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

