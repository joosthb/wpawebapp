from fastapi import FastAPI, Request, Form

from fastapi.templating import Jinja2Templates
from app.model import spell_number

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
def form_post(request: Request, num: int = Form(...)):
    result = spell_number(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

