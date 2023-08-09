from fastapi import FastAPI, Request, Form

from typing import Annotated

from fastapi.templating import Jinja2Templates
from app.model import wpa_psk

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/connections/{connection_id}")
async def read_connection(connection_id: int):
    return {"connection_id": connection_id}

@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post("/form")
async def gen_psk(request: Request, ssid: Annotated[str, Form()], password: Annotated[str, Form()]):
    result = wpa_psk(ssid, password)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.get("/psk")
async def get_psk(ssid: str, password: str):
    result = wpa_psk(ssid, password)
    return {"ssid": ssid, "psk": result}