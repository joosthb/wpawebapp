from binascii import hexlify
from hashlib import pbkdf2_hmac


def wpa_psk(ssid: str, password: str):
    dk = pbkdf2_hmac('sha1', str.encode(password), str.encode(ssid), 4096, 32)
    return (hexlify(dk).decode('ascii'))
