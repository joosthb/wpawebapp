# syntax=docker/dockerfile:1
FROM python:3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy app source as last step prevents rebuilding the whole image on code update.
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]