# syntax=docker/dockerfile:1
FROM python:3-alpine

WORKDIR /app

#RUN apk add --no-cache py-pip python3 

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy app source as last step prevents rebuilding the whole image on code update.
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]