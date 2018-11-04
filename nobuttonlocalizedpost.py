#!/usr/bin/python3
import json
import urllib.request
fcmUrl = 'https://fcm.googleapis.com/fcm/send'
rawbody = {
    "data": {
        "title-en" : "Hello",
        "description-en": "How do you do?",
        "title-i18n": "请联系客户支持 Nihao",
        "description-i18n":"请联系客户支持 Nihao ma?",
        "aT" : "3",
        "i" : "CAN",
	    "aN": "97520",
	    "aR": "3",
        "b-en" : "Buy",
        "b-i18n" : "Buy"
     },
    "registration_ids": ["fab9mycbmX8:APA91bEd8lkU5_50bNyPucx_herAfoaP_vPAZiVH6YPLvM45AerZAJQ5HFSTBBEUc7-PfxVDj5Fv4yyZ0kh0XXkbXN5WHmmRZhjomJziTeNobi-p6heM68JqVRFHUBnhuOHA-vfJqSKa"]
}
params = json.dumps(rawbody).encode('utf8')
req = urllib.request.Request(fcmUrl, data=params, headers={'Content-Type': 'application/json', 'Authorization': 'key=AAAAMG5BfPk:APA91bEWqPcLFwjCKEceRgMWVF8FIjZcljZleui5AJyxh83-yukJre_AjI6grtBnOqp0sVEa0nfv53i8H3AVEmqETYw5MJc_CA7g4vCcXugtDfu2iIpt3CYgC5MyyfaUtjwLkddwqxtkwOv58sfsDWIgi0hv8AQ3Vg'})
response = urllib.request.urlopen(req)
print(response.read().decode('utf8'))
