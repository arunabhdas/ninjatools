#!/usr/bin/python3
#

# import modules used here -- sys is a very standard one
import sys, argparse, logging
import json

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    
    print ("Hi. I'm Clipy. Please pass in the token as an argument to me")
    logging.info("You passed in the token")
    logging.debug("Your Token: %s" % args.argument)

    data = {}
    data['title-en'] = 'Hello'
    data['description-en'] = 'How do you do?'
    data['title-i18n'] = 'Nihao'
    data['description-i18n'] = 'Nihao ma?'
    data['aT'] = '3'
    data['i'] = 'CAN'
    data['aN'] = '97520'
    data['aR'] = '3'
    data['b-en'] = 'Buy'
    data['b-18n'] = 'Buy'
    json_data = json.dumps(data)

    rawbody = {}
    rawbody['data'] = data
    registration_ids = []
    registration_ids.append(args.argument)
    rawbody['registration_ids'] = registration_ids
    json_rawbody = json.dumps(rawbody)
    print(json_rawbody)

    params = json.dumps(json_rawbody).encode('utf8')
    req = urllib.request.Request(fcmUrl, data=params, headers={'Content-Type': 'application/json', 'Authorization': 'key=AAAAMG5BfPk:APA91bEWqPcLFwjCKEceRgMWVF8FIjZcljZleui5AJyxh83-yukJre_AjI6grtBnOqp0sVEa0nfv53i8H3AVEmqETYw5MJc_CA7g4vCcXugtDfu2iIpt3CYgC5MyyfaUtjwLkddwqxtkwOv58sfsDWIgi0hv8AQ3Vg'})
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf8'))
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser( 
        description = "Does a thing to some stuff.",
        epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
        fromfile_prefix_chars = '@' )
    parser.add_argument(
        "argument",
        help = "pass ARG to the program",
        metavar = "ARG")
    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    
    main(args, loglevel)