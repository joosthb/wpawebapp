# wpawebapp
Containerised web application written in python to manage wireless networks in a wpa_supplicant env.


---
Build and locally for dev:
```
docker build --tag wpawebapp .
docker run -p 8000:8000 -v ${PWD}:/app wpawebapp uvicorn app.main:app --reload --host 0.0.0.0
```