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
        "aT" : "1",
        "i" : "CAN",
	"aN": "97520",
	"aR": "0",
        "b-en" : "Buy",
        "b-i18n" : "Buy the package you want to buy Nyet iМожно по русски"
     },
    "registration_ids": ["cfmEIpjqomw:APA91bEQcUiFjrjoCcFQ-5UWPTR4hZE_Lko4N4-qQYlhqnpDi3CkdXfGLw-cvtYz8ePe1Okn4YygBmzmUFzl3S1cicIhARsLi-FkKoLSA7nzY0CKGhLC-gDlz_57n5B5rbT4M3EGyXVW"]
}
params = json.dumps(rawbody).encode('utf8')
req = urllib.request.Request(fcmUrl, data=params, headers={'Content-Type': 'application/json', 'Authorization': 'key=AAAAMG5BfPk:APA91bEWqPcLFwjCKEceRgMWVF8FIjZcljZleui5AJyxh83-yukJre_AjI6grtBnOqp0sVEa0nfv53i8H3AVEmqETYw5MJc_CA7g4vCcXugtDfu2iIpt3CYgC5MyyfaUtjwLkddwqxtkwOv58sfsDWIgi0hv8AQ3Vg'})
response = urllib.request.urlopen(req)
print(response.read().decode('utf8'))
