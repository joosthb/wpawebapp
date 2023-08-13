# wpawebapp
Containerised web application written in python to manage wireless networks in a wpa_supplicant env.

Build on fastapi and bootstrap.

---
Build and run locally for dev:
```
docker build --tag wpawebapp .
docker run --rm -p 8000:8000 -v ${PWD}:/app wpawebapp uvicorn app.main:app --reload --host 0.0.0.0
```