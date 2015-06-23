__author__ = 'shanecrossan'

from django_cron import CronJobBase, Schedule
from functions import *
from itieau_app.models import contact, Url
import requests

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 30 # every 30 mins

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'itieau_app.cons'    # a unique code

    def do(self):
        gateway = SmsGateway()
        gateway.loginDetails('shanecrossan@gmail.com', 'r33b00ts')

        url = Url.objects.filter(user__username = 'faaa')
        for url_obj in url:
            r = requests.get("http://107.170.192.206/" + url_obj.script)
            text = r.text.encode('ASCII', 'ignore')
            split_text = str.split(text, 'Bornier')
            value = split_text[url_obj.bornierSpilt][-5:]
            value_str = str.strip(value, '\x1e')
            value_float = float(value_str)
            message = 'Water level at ' + url_obj.name +' is less then 1m!'
            if value_float < 1:
                contact_obj = contact.objects.filter(user__username = 'faaa')
                for c_ob in contact_obj:
                    number = c_ob.number
                    gateway.sendMessageToNumber(number, message, '8659')