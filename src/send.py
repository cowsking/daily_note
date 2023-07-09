from flask import Blueprint, request
import requests
from src.history import notes
from src.database.database import db
send = Blueprint('send', __name__, url_prefix="/send")
from datetime import datetime

@send.post('/text')
def send_text():
    request_data = request.get_json()
    content = request_data['content']
    notes.append(content)
    headers = {
    'Content-type': 'application/json'
    }
    data = {
    'content': '#inbox\n{}'.format(content)
    }


    # 发送 POST 请求
    response = requests.post(
        'https://flomoapp.com/iwh/OTQw/9c99292b54e6acea7c11fb130c020e2a/', headers=headers, json=data)

    # 获取响应内容
    result = response.json()
    with db:
        with db.cursor() as cursor:
            insert_query = "INSERT INTO notes (date, note) VALUES (%s, %s)"

            values = (str(datetime.now().date()), content)

            cursor.execute(insert_query, values)

            
    return result

@send.get('/out')
def out():
    return notes[-1]

    