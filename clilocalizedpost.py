#!/usr/bin/python3
#

# import modules used here -- sys is a very standard one
import sys, argparse, logging
import json

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    
    print ("Hi. I'm Clipy. Please pass in the token as an argument to me")
    logging.info("You passed in the token")
    logging.debug("Your Argument: %s" % args.argument)

    data = {}
    data['key'] = 'value'
    json_data = json.dumps(data)
    print(json_data)
        
 
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