import requests
from rest_framework.utils import json


def send_order_email(data):
    dump_data = json.dumps(data)
    print(dump_data)
    try:
        r = requests.post('https://yshuynh2.pythonanywhere.com/send_order_email', data={'dump_data':dump_data}, timeout=0.1)
        # r = requests.post('http://localhost:1234/send_order_email', data={'dump_data':dump_data}, timeout=0.1)
    except Exception as e:
        print(str(e))
    return True
