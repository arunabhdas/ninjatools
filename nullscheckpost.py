#!/usr/bin/python3
import json
import urllib.request
fcmUrl = 'https://fcm.googleapis.com/fcm/send'
rawbody = {
    "data": {
        "title-en" : "Test Title",
        "description-en": "Test Description",
        "title-i18n": "请联系客户支持 Please do not send to all devices",
        "description-i18n":"请联系客户支持 Support",
        "aT" : "1"
     },
    "registration_ids": ["dALtl7qgqCM:APA91bHCkbAUXYlIPbA4lXFb9ABJCVs1cedR642Th7J2tgMB5gQXBgk9hwWb5pLtouEWSH7qhjHkno8a8TKzyY8fDJC8aHs-Vnh-5CAsD6Uuft9j4WOc5zlN4osOuAbWGkzwsyMAbGCA"]
}
params = json.dumps(rawbody).encode('utf8')
req = urllib.request.Request(fcmUrl, data=params, headers={'Content-Type': 'application/json', 'Authorization': 'key=AAAAMG5BfPk:APA91bEWqPcLFwjCKEceRgMWVF8FIjZcljZleui5AJyxh83-yukJre_AjI6grtBnOqp0sVEa0nfv53i8H3AVEmqETYw5MJc_CA7g4vCcXugtDfu2iIpt3CYgC5MyyfaUtjwLkddwqxtkwOv58sfsDWIgi0hv8AQ3Vg'})
response = urllib.request.urlopen(req)
print(response.read().decode('utf8'))
