#! /usr/bin/python3

import imaplib
import configparser
import os


def open_connection(verbose=True):
    # Read the config file
    config = configparser.ConfigParser()
    config.read([os.path.expanduser('~/.pymotw')])

    # Connect to the server
    hostname = ('imap.gmail.com')
    if verbose:
        print('\n')
        print('Connecting to', hostname)
    server = imaplib.IMAP4_SSL(hostname)

    # Login to our account
    # ENTER YOUR EMAIL
    email_account = ('xxxxxx@gmail.com')
    # ENTER YOUR PASSWORD
    password = ('xxxxx')
    if verbose:
        print('Logging in as', email_account)
        print('\n')
    server.login(email_account, password)
    return server

# prints results of def open_connection
if __name__ == '__main__':
    with open_connection(verbose=True) as c:
        print(c)
