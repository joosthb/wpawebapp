from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from typing import Annotated
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

#Static file serv
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates/")

@app.get("/")
def root(request: Request, session: Session = Depends(get_session)):
    connections = session.query(models.Connection).all()
    return templates.TemplateResponse('connections.html', context={'request': request, 'connections': connections})

@app.post("/add")
async def createConnection(request: Request, ssid: Annotated[str, Form()], password: Annotated[str, Form()], session = Depends(get_session)):
    itemObject = models.Connection(ssid = ssid, psk = wpa_psk(ssid, password))
    session.add(itemObject)
    session.commit()
    session.refresh(itemObject)
    connections = session.query(models.Connection).all()
    return templates.TemplateResponse('connections.html', context={'request': request, 'connections': connections})

@app.get("/remove/{id}")
def removeConnection(request: Request, id:int, session = Depends(get_session)):
    itemObject = session.query(models.Connection).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    connections = session.query(models.Connection).all()
    return templates.TemplateResponse('connections.html', context={'request': request, 'connections': connections})

@app.get("/connections")
def getConnections(session: Session = Depends(get_session)):
    connections = session.query(models.Connection).all()
    return connections

@app.get("/wpa_supplicant.conf")
def get_wpa_sup(request: Request, session: Session = Depends(get_session)):
    connections = session.query(models.Connection).all()
    return templates.TemplateResponse('wpa_supplicant.conf', context={'request': request, 'connections': connections})
