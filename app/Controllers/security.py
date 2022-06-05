import requests
from app import app
import json
import hashlib
import secrets
import datetime
import qrcode
import base64
import io


def sendImageToMediaServer(data):
    addr = app.config['MEDIA_SERVER_ADDRESS']
    r = requests.post(addr+"/create_image",
                      data='{"base64":"' + str(data)+'"}')
    print(r.json()['name'])

    return (r.json()['name'])


def remImageFromMediaServer(name):
    addr = app.config['MEDIA_SERVER_ADDRESS']
    r = requests.post(addr+"/delete_image", data='{"url":"' + str(name)+'"}')
    print(*r)


def generateToken(power):
    return secrets.token_hex(power)


def makeQrCode(data):
    img = qrcode.make(data)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    qr_code = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return sendImageToMediaServer(qr_code)
