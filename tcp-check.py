#!/usr/bin/env python3

import sys
import socket

ARGUMENTS_START_SINCE = 1
REQUIRED_ARGUMENTS_COUNT = 2
VERBOSE_MODE = None

ERR__NO_ERROR = 0
ERR__NO_ARGUMENTS_SPECIFIED = 1
ERR__NOT_ENOUGHT_ARGUMENTS = 2
ERR__CANNOT_PARSE_ARGUMENTS = 3
ERR__CANNOT_CONNECT = 4
ERR__SOMETHING_ELSE = 5


def help():
    print("tcp-check.py <host> <port> [verbose|silent]")


def PrintIfVerbose(msg):
    if VERBOSE_MODE:
        print(msg)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # no parameters specified
        PrintIfVerbose("Error: no parameters specified - show help.")
        help()
        sys.exit(ERR__NO_ARGUMENTS_SPECIFIED)
    if sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "-help" or sys.argv[1] == "/?":
        # requested help about program
        PrintIfVerbose("Help is requested by parameter \"{}\"." . format(sys.argv[1]))
        help()
        sys.exit(ERR__NO_ERROR)
    if len(sys.argv) < ARGUMENTS_START_SINCE+REQUIRED_ARGUMENTS_COUNT:
        # not enought arguments
        PrintIfVerbose("Error: not enought arguments =", sys.argv[1:])
        help()
        sys.exit(ERR__NOT_ENOUGHT_ARGUMENTS)
    if len(sys.argv) >= ARGUMENTS_START_SINCE+3:
        if sys.argv[ARGUMENTS_START_SINCE+2] == "verbose":
            VERBOSE_MODE = True
        elif sys.argv[ARGUMENTS_START_SINCE+2] == "silent":
            VERBOSE_MODE = False

    try:
        # parse command line arguments
        server = sys.argv[ARGUMENTS_START_SINCE + 0]
        port = int(sys.argv[ARGUMENTS_START_SINCE + 1])
    except:
        # probably letters instead of port number
        PrintIfVerbose("Error: cannot parse arguments =", sys.argv[1:])
        sys.exit(ERR__CANNOT_PARSE_ARGUMENTS)

    result = ERR__SOMETHING_ELSE
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((server, port))
        if result == 0:
            PrintIfVerbose("Info: successfully connected to {}:{}." . format(server, port))
        else:
            raise socket.error
    except:
        PrintIfVerbose("Error: cannot connect to {}:{}." . format(server, port))
        result = ERR__CANNOT_CONNECT
    finally:
        sock.close()

    sys.exit(result)

