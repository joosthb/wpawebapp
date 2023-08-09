import hashlib, binascii
def wpa_psk(ssid: str, password: str):
    dk = hashlib.pbkdf2_hmac('sha1', str.encode(password), str.encode(ssid), 4096, 32)
    return (binascii.hexlify(dk))
