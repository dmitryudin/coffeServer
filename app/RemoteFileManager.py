from fileinput import filename
from app import app
from flask import request
import json
from app import model, db
from app import security as scr
import datetime
from flask import jsonify
import random
import string
import os

def buildRandomString(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))



@app.route('/delete_file', methods=['POST'])
def deleteFile():
    print('endpoint')
    recvData = request.get_data().decode('utf-8')
    jsonData = json.loads(recvData)
    os.remove('/var/www/html/'+jsonData['url'].split('/')[-1])
    return '{"status":"ok"}'


@app.route('/upload_file', methods=['POST'])
def uploadFile():
    '''
    пишет изображение в файл и возвращает его url
    '''
    uploadedFile = request.files['image']
    filename = buildRandomString(30)+'.png'

    uploadedFile.save('/var/www/html/'+filename)

    return app.config['MEDIA_SERVER_ADDRESS']+'/'+filename