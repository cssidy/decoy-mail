#! /usr/bin/python3

import imaplib
from login_credentials import gmail_credentials


def open_imap_connection(verbose=True):
    # Connect to the imap server
    hostname = 'imap.gmail.com'
    if verbose:
       print('\n')
       print('Connecting to', hostname)
    imap_server = imaplib.IMAP4_SSL(hostname)

    # Login to email account
    if verbose:
        print('Logging in as', gmail_credentials.get('username', 0))
    imap_server.login(gmail_credentials.get('username', 0), gmail_credentials.get('password', 0))
    print('Success.')



