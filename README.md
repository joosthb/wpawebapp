# wpawebapp
Containerised web application written in python to manage wireless networks in a wpa_supplicant env.


---
Build locally
```
docker build --tag wpawebapp .
```

Run locally
```
docker run -p 8080:80 wpawebapp 
```