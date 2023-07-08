from flask import Blueprint, request
import requests


auth = Blueprint('auth', __name__, url_prefix="/send")


@auth.post('/text')
def chat():
    request_data = request.get_json()
    content = request_data['content']

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

    return result

