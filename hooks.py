from os import environ as env
import requests
import time
import settings
from os import environ as env
from erp import req_args
   
def notices_updated(notices):
    for notice in notices:
        message = {
            'to': env['NOTICES_EMAIL_ADDRESS'],
            'from': 'no-reply@mftp.herokuapp.com',
            'fromname': 'MFTP',
            'subject': 'Notice: %s - %s' % (notice['subject'],
                                            notice['company']),
        }
        files = []
        if 'attachment_url' in notice:
            filename = "attachment.pdf"
            files = [('attachment', (filename, notice['attachment_raw']))]

        r = requests.post(env['SEND_MESSAGE_URL'],data={
            "message":notice['text'],
            "number":9354817605
        },verify=False)
        if 'attachment_url' in notice:
            r = requests.post(env['SEND_FILE_URL'],files={"attachment":notice['attachment_raw']})
        
        time.sleep(10)

        print ('Sent notice to', message['to'], ':', message['subject'], r.text)
