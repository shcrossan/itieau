__author__ = 'shanecrossan'

from django_cron import CronJobBase, Schedule
from functions import *
from models import contact
import requests

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 2 # every 30 mins

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'itieau_app.cons'    # a unique code

    def do(self):
        gateway = SmsGateway()
        gateway.loginDetails('shanecrossan@gmail.com', 'r33b00ts')


        r = requests.get("http://107.170.192.206/tiapiriuf.php")
        text = r.text.encode('ASCII', 'ignore')
        split_text = str.split(text, 'Bornier local')
        value = split_text[0][-5:]
        value_str = str.strip(value, '\x1e')
        value_float = float(value_str)
        message = 'Water level at Tiapiri is less then 1m **test if loop User**!'

        if value_float > 1:
            contact_obj = contact.object.filter(User='faaa')
            for c_ob in contact_obj:
                number = c_ob.number
                gateway.sendMessageToNumber(number, message, '8659')