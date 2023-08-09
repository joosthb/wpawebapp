from pydantic import BaseModel

class Connection(BaseModel):
   ssid: str
   psk: str
