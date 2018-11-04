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
        "aT" : "2",
        "i" : "CAN",
	    "aN": "97520",
	    "aR": "3",
        "b-en" : "Buy",
        "b-i18n" : "Buy"
     },
    "registration_ids": ["e2diR1GCVNA:APA91bHTUh9t1tFl1EMSLNuwrm5Yz_S9bkKsumCg7poO33mgQssbHSLYv1oyIdVEKSJwlO1AeLIiQoAjQzAgDyDphpb9czO6Ty2EB3n-wIBP8vISu91AkDuSzPijHonmhV0_xu8Lz37I"]
}
params = json.dumps(rawbody).encode('utf8')
req = urllib.request.Request(fcmUrl, data=params, headers={'Content-Type': 'application/json', 'Authorization': 'key=AAAAMG5BfPk:APA91bEWqPcLFwjCKEceRgMWVF8FIjZcljZleui5AJyxh83-yukJre_AjI6grtBnOqp0sVEa0nfv53i8H3AVEmqETYw5MJc_CA7g4vCcXugtDfu2iIpt3CYgC5MyyfaUtjwLkddwqxtkwOv58sfsDWIgi0hv8AQ3Vg'})
response = urllib.request.urlopen(req)
print(response.read().decode('utf8'))
