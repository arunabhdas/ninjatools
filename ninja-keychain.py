#!/usr/bin/env python3
import sys, argparse, logging
import keyring

def main(args, loglevel):

    keyring.set_password('keychain_demo', 'test', 'thisisnotsecure')

    print(keyring.get_password('keychain_demo', 'test'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description = "./ninja-keychain",
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
    args = parser.parse_args()
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    main(args, loglevel)

