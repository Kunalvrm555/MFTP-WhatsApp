from os import environ as env
import requests
import time
import settings
from os import environ as env
from erp import req_args
   
def notices_updated(notices):
    for notice in notices:
        r = requests.post(env['SEND_MESSAGE_URL'],data={
            "message":notice['text'],
        },verify=False)
        if 'attachment_url' in notice:
            r = requests.post(env['SEND_FILE_URL'],files={"attachment":notice['attachment_raw']})
        
        time.sleep(10)
