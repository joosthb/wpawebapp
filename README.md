# wpawebapp
Containerised web application written in python to manage wireless networks in a wpa_supplicant env.

Build on fastapi and bootstrap.

## Configuration
compose.yml example
```
version: '3'
services:
  wpawebapp:
    container_name: wpawebapp
    image: joosthb/wpawebapp
    restart: unless-stopped
    ports:
      # ingress port webgui
      - "8000:8000/tcp"
    volumes:
      # target config on host
      - /etc/wpa_supplicant/wpa_supplicant-wlan0.conf:/app/wpa_supplicant.conf
      # connections database - mount for persistence.
      - ~/connections.db:/app/connections.db
      # named pipe to control services on docker host
      - ~/containerpipe:/containerpipe
```
Named pipe is described in [joosthb/digital_herbert](github.com/joosthb/digital_herbert).

## Troubleshooting
---
Build and run locally for dev:
```
docker build --tag wpawebapp .
docker run --rm -p 8000:8000 -v ${PWD}:/app wpawebapp uvicorn app.main:app --reload --host 0.0.0.0
```

List current configured connections
```
wpa_cli list_networks
```

