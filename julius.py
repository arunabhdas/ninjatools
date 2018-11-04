#!/usr/bin/python3
#

# import modules used here -- sys is a very standard one
import sys, argparse, logging
import json
import urllib.request
def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    
    fcmUrl = 'https://fcm.googleapis.com/fcm/send'
    print ("Woof. I'm Julius. Please feed me registration token as an argument to me")
    logging.info("You passed in the token")
    logging.debug("Your Token: %s" % args.token)

    data = {}
    data['title-en'] = args.subject
    data['description-en'] = args.desc 
    data['title-i18n'] = args.subject
    data['description-i18n'] = args.desc
    data['aT'] = args.action 
    data['i'] = 'CAN'
    data['aN'] = '97520'
    data['aR'] = args.route
    data['b-en'] = args.button
    data['b-i18n'] = args.button
    json_data = json.dumps(data)

    rawbody = {}
    rawbody['data'] = data
    registration_ids = []
    registration_ids.append(args.token)
    rawbody['registration_ids'] = registration_ids
    json_rawbody = json.dumps(rawbody)
    print(json_rawbody)

    params = json.dumps(rawbody).encode('utf8')
    req = urllib.request.Request(fcmUrl, data=params, headers={'Content-Type': 'application/json', 'Authorization': 'key=AAAAMG5BfPk:APA91bEWqPcLFwjCKEceRgMWVF8FIjZcljZleui5AJyxh83-yukJre_AjI6grtBnOqp0sVEa0nfv53i8H3AVEmqETYw5MJc_CA7g4vCcXugtDfu2iIpt3CYgC5MyyfaUtjwLkddwqxtkwOv58sfsDWIgi0hv8AQ3Vg'})
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf8'))
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser( 
        description = "./julius.py --token @params.conf --subject Goodmorning --desc Zaoshanghao --action 0 --route 3 --button Update",
        epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
        fromfile_prefix_chars = '@' )

    #parser.add_argument(
    #    "argument",
    #    help = "pass ARG to the program",
    #    metavar = "ARG")
    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")
    parser.add_argument('-t', '--token',
                    default='fhE1a6AjNU4:APA91bHRrXfVwI2e4gQXtdis0Z-VIeaxuhPKeOMtYecKzxnJuTO2fGbNGL3EJkIQncpdSXWUf0sePOEWTz8Fdfhxy8jhe9QCawnMx0gTPsjPguz_eTjNP_IuZuPLHr5YqxbjMiKxMACU',
                    required=False,
                    help='device token') 
    parser.add_argument('-s', '--subject',
                    default='Hello',
                    required=False,
                    help='subject of notification')
    parser.add_argument('-d', '--desc',
                    default='Hello',
                    required=False,
                    help='desc of notification')
    parser.add_argument('-a', '--action',
                    default=0,
                    required=False,
                    help='action of notification')
    parser.add_argument('-r', '--route',
                    default='3',
                    required=False,
                    help='activity route')
    parser.add_argument('-b', '--button',
                    default='Update',
                    required=False,
                    help='button text')
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    
    main(args, loglevel)
