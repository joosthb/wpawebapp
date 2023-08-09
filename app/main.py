from fastapi import FastAPI, Request, Form
from typing import Annotated
from fastapi.templating import Jinja2Templates

from app.model import wpa_psk
from app.schemas import Connection

data = []

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/connection")
def add_connection(connection: Connection):
   data.append(connection.dict())
   return data

@app.get("/connections")
def get_connections():
   return data

@app.get("/connection/{id}")
def get_connection(id: int):
   return data[id]

@app.delete("/connection/{id}")
def delete_connection(id: int):
   data.pop(id)
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

