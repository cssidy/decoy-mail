#! /usr/bin/python3

import imaplib
from login_credentials import gmail_credentials
# import configparser
# import os


def open_connection(verbose=True):
    # Read the config file
    # config = configparser.ConfigParser()
    # config.read([os.path.expanduser('~/.pymotw')])

    # Connect to the server
    hostname = ('imap.gmail.com')
    if verbose:
        print('\n')
        print('Connecting to', hostname)
    server = imaplib.IMAP4_SSL(hostname)

    # Login to our account
    email_account = ()
    password = ()
    if verbose:
        print('Logging in as', gmail_credentials.get('username', 0))
        print('\n')
    server.login(gmail_credentials.get('username', 0), gmail_credentials.get('password', 0))
    return server

# prints results of def open_connection
if __name__ == '__main__':
    with open_connection(verbose=True) as c:
        print(c)
