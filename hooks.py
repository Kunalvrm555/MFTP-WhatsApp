from os import environ as env
import requests
import base64
import time
import settings
from os import environ as env
from erp import req_args
   
def notices_updated(notices):
    for notice in notices:
        if ('attachment_url') in notice:
            encoded_string = base64.b64encode(notice['attachment_raw'])
            r = requests.post(env['SEND_FILE_URL'],data={'base64string':encoded_string},stream=True)
            print("Attachment sent")
        r = requests.post(env['SEND_MESSAGE_URL'],data={
            "message": notice['text']+'\n'+notice['time'],
        },verify=False)
        time.sleep(5)
