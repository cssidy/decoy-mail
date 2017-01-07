#! /usr/bin/python3

import imaplib
import pprint
from login_credentials import gmail_credentials


def start_imap_connection():
    # Connect to the imap server
    hostname = 'imap.gmail.com'
    print('\n')
    print('Connecting to', hostname)
    imap_server = imaplib.IMAP4_SSL(hostname)

    # Login to email account
    print('Logging in as', gmail_credentials.get('username', 0))
    imap_server.login(gmail_credentials.get('username', 0), gmail_credentials.get('password', 0))
    print('Success.')

start_imap_connection()

